#!/bin/bash



function battery()
{
    notify-send -a "sababa" --icon=battery-$1 -u $2 "battery $1"
}
battery low critical
battery good normal
battery full low

# test word wrap
msg="Lorem7 ipsum7 dolor7 sit7 amet,7 consectetur7 adipiscing7 elit.7 Aenean7 placerat7 gravida7 justo7 eget7 sodales.7 Cras7 nec7 diam7 nec7 lectus7 consectetur7 rhoncus7 at7 ac7 dolor.7 Ut7 placerat7 felis7 vitae7 diam7 ornare,7 in7 vestibulum7 tortor7 sagittis.7 Aenean7 sed7 metus7 ultrices,7 varius7 quam7 ultrices,7 blandit7 tortor.7 Nam7 pulvinar7 est7 non7 varius7 hendrerit.7 Praesent7 quis7 dui7 nisi.7 Donec7 id7 fringilla7 orci,7 nec7 blandit7 ipsum.7 Etiam7 sed7 egestas7 orci.7 Etiam7 augue7 justo,7 suscipit7 ac7 ligula7 id,7 aliquet7 posuere7 risus.7 In7 hac7 habitasse7 platea7 dictumst.7 Aliquam7 eu7 convallis7 odio.7 Morbi7 vestibulum,7 quam7 ac7 iaculis7 gravida,7 sapien7 elit7"
notify-send -u critical "split words" "$msg"

msg="Lorem7ipsum7dolor7sit7amet7consectetur7adipiscing7 elit.7 Aenean7 placerat7 gravida7 justo7 eget7 sodales.7 Cras7 nec7 diam7 nec7 lectus7 consectetur7 rhoncus7 at7 ac7 dolor.7 Ut7 placerat7 felis7 vitae7 diam7 ornare,7 in7 vestibulum7 tortor7 sagittis.7 Aenean7 sed7 metus7 ultrices,7 varius7 quam7 ultrices,7 blandit7 tortor.7 Nam7 pulvinar7 est7 non7 varius7 hendrerit.7 Praesent7 quis7 dui7 nisi.7 Donec7 id7 fringilla7 orci,7 nec7 blandit7 ipsum.7 Etiam7 sed7 egestas7 orci.7 Etiam7 augue7 justo,7 suscipit7 ac7 ligula7 id,7 aliquet7 posuere7 risus.7 In7 hac7 habitasse7 platea7 dictumst.7 Aliquam7 eu7 convallis7 odio.7 Morbi7 vestibulum,7 quam7 ac7 iaculis7 gravida,7 sapien7 elit7"
notify-send -u low "long word" "$msg"
