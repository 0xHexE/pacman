self.description = "Install a sync package conflicting with a local one"

sp = pmpkg("pkg1")
sp.conflicts = ["pkg2"]
self.addpkg2db("sync", sp);

lp = pmpkg("pkg2")
self.addpkg2db("local", lp);

self.args = "-S pkg1"

self.addrule("PACMAN_RETCODE=0")
self.addrule("PKG_EXIST=pkg1")
self.addrule("!PKG_EXIST=pkg2")
