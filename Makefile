init:
	pip install -r requirements.txt
	[ -d sample ] || mkdir sample && wget --directory-prefix=sample http://www.xbrlsite.com/US-GAAP/BasicExample/2010-09-30/abc-20101231_All.zip && cd sample && unzip ./abc-20101231_All.zip && cd ../
run-sample:
	./xbrl2oracle ./sample/abc-20101231.xml

