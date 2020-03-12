#!/usr/local/bin/spatch-wrapper --timeout 120 -j 0
@initialize:python@
@@
def csv_pos(p, p1):
    return p[0].line + "," + p1[0].line_end
allowed = set()

fp = open("found_till", "r")
for line in fp:
    allowed.add(line.rstrip())
fp.close()
@r1@
identifier bar;
position start,end;
@@
bar@start(...)@end;

@script:python@
fun << r1.bar;
start << r1.start;
end << r1.end;
@@
if fun in allowed:
    print(csv_pos(start, end) + "\n")