#!/usr/bin/python2
def kl():

	s1="""?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<!-- Put site-specific property overrides in this file. -->

	<configuration>
	<property>
	<name>fs.default.name</name>
	<value>hdfs://{0}:10001</value>
	</property>

	</configuration>""" .format(ip)
