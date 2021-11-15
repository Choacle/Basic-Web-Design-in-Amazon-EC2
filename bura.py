from flask import Flask, render_template
from ec2_metadata import ec2_metadata
from flask import request

app=Flask(__name__)

headings = ('METADATA','VALUE')

instanceID=ec2_metadata.instance_id
ami_launch_index=ec2_metadata.ami_launch_index
public_hostname=ec2_metadata.public_hostname
public_ipv4=ec2_metadata.public_ipv4
local_hostname=ec2_metadata.private_hostname
local_ipv4=ec2_metadata.private_ipv4


data = (
	('instance-id',instanceID),
	('ami-launch-index',ami_launch_index),
	('public-hostname',public_hostname),
	('public-ipv4',public_ipv4),
	('local-hostname',local_hostname),
	('local-ipv4',local_ipv4)
)

@app.route('/')
def table():
	return render_template('bura.html', headings=headings, data=data)

if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)