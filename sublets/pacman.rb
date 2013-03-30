# Pacman sublet file
# Created with sur-0.2
configure :pacman do |s|
  s.icon = Subtlext::Icon.new( "pacman.xbm" )

  s.interval =   s.config[:interval]   || 3600
  s.separator =  s.config[:separator]  || " // "
  s.updatefile = s.config[:updatefile] || "#{ENV['HOME']}/.pacmanupdates"
end

helper do |s|
  def updates
    # Open file
    f = File.open( self.updatefile, "r" )
    h = Hash.new

    # Fill hash, just in case there are no updates
    h['core'] = 0
    h['extra'] = 0
    h['community'] = 0

    # Count occurences of "core", "extra" and "community" in details
    f.each_line { |line|
      words = line.split( /\/ */ )
      words.each { |w|
        if h.has_key?(w)
          h[w] = h[w] + 1
        else
          h[w] = 1
        end
      }
    }

    f.close

    self.data = self.icon + ' ' + h['core'].to_s + self.separator + h['extra'].to_s + self.separator + h['community'].to_s
  end
end

on :run do |s|
  updates
end
#  vim: set ts=2 sw=2 tw=0 :
