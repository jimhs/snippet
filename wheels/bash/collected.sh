#!/bin/bash

# history汇总
cat .bash_history | awk '{print $1}' | sort | uniq -c | sort -n > ~/bash/.bash_hitory_trimmed