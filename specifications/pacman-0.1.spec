# -*- encoding: utf-8 -*-
# Pacman specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Pacman"
  s.version     = "0.1"
  s.tags        = [ ]
  s.files       = [ "pacman.rb" ]
  s.icons       = [ "pacman.xbm" ]

  # Sublet description
  s.description = "Display pacman available updates"
  s.notes       = <<NOTES
Show updates available in Archs pacman package manager
Needs this: https://gist.github.com/952010 run as a cronjob
NOTES

  # Sublet authors
  s.authors     = [ "crshd" ]
  s.contact     = "crshd@mail.com"
  s.date        = "Mon May 02 23:17 MYT 2011"

  # Sublet config
  s.config = [
    {
      :name        => "interval",
      :type        => "integer",
      :description => "Update interval",
      :def_value   => "3600"
    },
    {
      :name        => "separator",
      :type        => "string",
      :description => "String to seperate repos",
      :def_value   => " // "
    },
    {
      :name        => "updatefile",
      :type        => "string",
      :description => "File that holds pacman update info",
      :def_value   => "#{ENV['HOME']}/.pacmanupdates"
    }
  ]

  # Sublet grabs
  #s.grabs = {
  #  :PacmanGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end
