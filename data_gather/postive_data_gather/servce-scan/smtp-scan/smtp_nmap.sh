#!/bin/bash

#must under the condition that we have fonud the destion open the 25 port
#usage:
if [ ${1} == 1 ]; then
				nmap ${2} --script smtp-enum-users.nse --script-args=smtp-enum-users.methods={VRFY} -p 25

elif [[ ${1} == 2 ]]; then
				nmap -p 25 --script=smtp-brute.nse ${1} 
fi

	

