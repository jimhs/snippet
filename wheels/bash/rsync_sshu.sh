#!/usr/bin/env bash

source $HOME/.self/.exports

for folder in $BK_FOLDERS
do
	if [ -d "$HOME_$folder" ]
	then
		echo -e "chec-ing \033[36m$SSH_$folder\033[00m"
		# strip off tailing semi-colon
		SSH="${SSH_%:}"
		# if folder not exist, creat it and set 700
		ssh $SSH "if [ ! -d $folder ]; then mkdir $folder ; chmod 700 $folder ; fi"
		echo -e "sync-ing \033[36m$folder [ $HOME_ --> $SSH ]\033[00m"
		rsync -avz --delete $HOME_$folder $SSH_$folder
	fi
done

echo "done"
