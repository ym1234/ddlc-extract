cat $1 | strings | grep '^.*r$' | grep -v '^D:.*$' | grep -Ev '^h.{3}$'| grep -v '^ch\d+_.*$' | grep -v '^=.*$' | less
