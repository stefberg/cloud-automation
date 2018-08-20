#!/bin/sh

# Script to generate some requests to a http to do a really small scale DDoS to test restrictions enabled on the site.

url=$1
tps=$2
limit=$3
if [ -z "$limit" ]
then
    echo "Usage: $0 <url> <tps> <limit in secs>"
    exit 1
fi
i=0
while [ $i -lt $limit ]
do
    i=$(($i + 1))
    t=0
    while [ $t -lt $tps ]
    do
	full_url="$url?http_reqtest=true&round_$i&tpsi=$t"
	( echo $full_url; curl -s --insecure "$full_url" | wc) >> http_request_log.txt &
	t=$(($t + 1))
    done
    sleep 1
done
