# cat $1 | strings | grep '^.*r$' | grep -v '^D:.*$' | grep -Ev '^.{3}r$' | grep -v '^ch\d*.*$' | grep -v '^=.*$' | grep -v '^J(0yYK.*$' | grep -v 'NN]NN]tr' | grep -v '^WK.*$'
# cat $1 | strings | grep '^.*r$' | grep -vE -e '^D:.*$' -e '^.{3}r$' -e 'ch\d*.*' -e '^=.*$' | less
# removes some actual dialouge, this is really a hack until i figure out how to parse 'em
# pipe through uniq or sort -u to remove duplicates
cat $1 | strings | grep '^.*r$' | grep -Ev -e '^D:.*$' -e '^.{3}r$' -e '^ch\d*.*$' -e '^=.*$' -e '^J\(0yYK.*$'  -e 'NN]NN]tr' -e '^WK.*$'
