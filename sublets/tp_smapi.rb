# Tp_smapi sublet file
# Created with sur-0.2
configure :tp_smapi do |s|
  s.interval    	= s.config[:interval]		|| 1
  s.path 	      	= ""
  s.format_string = s.config[:format_string]	|| "%power_now% - %temperature% - %voltage%"

  # Find path to battery
  begin
    s.path = s.config[:path] || Dir["/sys/devices/platform/smapi/BAT*"].first
  rescue => err
    puts err, err.backtrace
    raise "Could not find tp_smapi directory"
  end

  # Parse format string
  fields = [ "power_now", "power_avg", "temperature", "voltage", "current_now", "current_avg" ]

  s.format_values = []

  s.format_string.gsub!(/%([^%]+)%/) do
    field = $1
    out   = ""

    if (fields.include?(field))
      # Add fields to s.format_values
      s.format_values << field
      # Insert placeholders and unit symbols into s.format_string
      case field
      when "power_now", "power_avg"
        out = "%sW"
      when "temperature"
        out = "%s°C"
      when "voltage" 
        out = "%sV"
      when "current_now", "current_avg"
        out = "%sA"
      end

    end
  end

end

on :run do |s|
  begin
    # Check if battery is installed
    if IO.readlines(s.path + "/installed").first.to_i == 0
      then s.data = "-- battery not installed --"
    else

      # Read in values
      values = s.format_values.dup
      values.map! do |k|
        (IO.readlines(s.path + "/" + k).first.to_f/1000).round(1)
      end

      # Assemble data string
      s.data = s.format_string % values
    end
  rescue => err # Sanitize to prevent unloading
    s.data = "tp_smapi"
    p err
  end
end
