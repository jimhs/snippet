#!/bin/bash
#unfinished

declare -a arr

src="$HOME/"
dest="$HOME/snippets/dots"
for i in $(ls -A $dest)
do
	if [ -f $src/$i ]; then
		dest_inode=$(ls -li $i | cut -d ' ' -f 1);
		src_inode=$(ls -li $src/$i | cut -d ' ' -f 1);
		echo -n $i '--'
		test $dest_inode = $src_inode \
		&& echo 'ok' \
		|| echo 'xx';
	fi
done;