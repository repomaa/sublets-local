# -*- encoding: utf-8 -*-
# Tp_smapi specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Tp_smapi"
  s.version     = "0.1"
  s.tags        = [ ]
  s.files       = [ "tp_smapi.rb" ]
  s.icons       = [ ]

  # Sublet description
  s.description = "Show tp_smapi information"
  s.notes       = <<NOTES
This sublet displays battery status information on IBM/Lenovo Thinkpads using the sysfs interface of the tp_smapi module.

Format string
-------------

The output of the sublet can be customized by a format_string. Following fields are allowed alongside all kind of text.

%power_now% 	- current power
%power_avg% 	- last minute power average
%temperature% 	- battery temperature
%voltage% 	- battery voltage
%current_now% 	- momentary current
%current_avg% 	- last minute current average

Examples:

%power_now% - %temperature%
%voltage% %current_now%

NOTES

  # Sublet authors
  s.authors     = [ "Fabian Schmid" ]
  s.contact     = "fabian.schmid@tum.de"
  s.date        = "Wed Apr 11 14:13:15 CEST 2012"

  # Sublet config
  s.config = [
    {
      :name        => "path",
      :type        => "string",
      :description => "Path to the battery directory of tp_smapi",
      :def_value   => "/sys/devices/platform/smapi/BAT0"
    },
    {
      :name 	   => "format_string",
      :type        => "string",
      :description => "Output format string",
      :def_value   => "%power_now% - %temperature% - %voltage%"
    }
  ]

  # Sublet grabs
  #s.grabs = {
  #  :Tp_smapiGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end
