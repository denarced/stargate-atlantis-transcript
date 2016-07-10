#!/bin/bash

# In these episodes, the generic "WRAITH:" refers only to Todd
sed -i 's|^WRAITH:|TODD:|' text/408.md text/409.md text/411.md

# In this episode, the generic "WRAITH:" refers to at least two characters. In
# the beginning Todd is referred to, later it's another character, and in the
# end Todd is no longer referred in generic manner; "TODD:" is used.
sed -i '1,/^ATLANTIS CONTROL ROOM/ s|^WRAITH:|TODD:|' text/412.md

# Remove end of line spaces as they're not necessary in markdown
sed -i 's|[[:blank:]]\+$||' text/*.md
