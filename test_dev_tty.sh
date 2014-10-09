    #!/bin/bash
    printf "Enter new password: "    #ÌʾÊÈ
    stty -echo                               #¹رÕԶ¯´òä×·ûÄ
    read password < /dev/tty         #¶Á¡ÃÂ
    printf "\nEnter again: "             #»»Ðºó¾ÔÊÈһ´Î    read password2 < /dev/tty       #Ô¶Á¡һ´ÎÔ·È
    printf "\n"                               #»»Ð
    stty echo                                #¼ÇŴòԶ¯´òä×·ûÄ
    echo "Password = " $password #Ê³öë
    echo "Password2 = " $password2
    echo "All Done"
