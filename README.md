# README

Splunk Connect for SNMP MIB Server is an open source packaged component for of Splunk Connect for SNMP.
This project contains a community collection of SNMP MIBs.

## Purpose

This project is a repository of MIBS packaged as a OCI compliant container for use with Splunk Connect for SNMP


## Usage

This project is only intended to be used as part of a Splunk Connect for SNMP Deployment

## Support

Splunk Connect for SNMP is an open source product developed by Splunkers with contributions from the community of partners and customers. This unique product will be enhanced, maintained and supported by the community, led by Splunkers with deep subject matter expertise. The primary reason why Splunk is taking this approach is to push product development closer to those that use and depend upon it. This direct connection will help us all be more successful and move at a rapid pace.

Post a question to Splunk Answers using the tag "Splunk Connect For SNMP"

Join the #splunk-connect-for-snmp room in the splunk-usergroups Slack Workspace. If you don't yet have an account [sign up](https://docs.splunk.com/Documentation/Community/1.0/community/Chat)

Please use the GitHub issue tracker to submit bugs or request enhancements: https://github.com/splunk/splunk-connect-for-snmp-mib-server/issues

Get involved, try it out, ask questions, contribute filters, and make new friends!

## Contributing

We welcome feedback and contributions from the community! Please see our [contribution guidelines](CONTRIBUTING.md) for more information on how to get involved.

## License

* Individual MIBs licensed as indicated

* NGNIX [BSD-2-Clause](https://hub.docker.com/_/nginx/)



## Development Instructions for Mib Server

> This is used as a reference steps while working on development aspects of SNMP Mib Server component of Splunk Connect for SNMP!

#### Get Started
```
git clone git@github.com:splunk/splunk-connect-for-snmp-mib-server.git
cd "splunk-connect-for-snmp-mib-server"
```

#### Run MongoDB

```docker run -d -p 27017:27017 -v ./data:/data/db mongo```

#### Setup Environment for Mib Server
```
export MONGO_URI=mongodb://host:27017
export MIBS_FILES_URL=http://0.0.0.0:5000/files/asn1/@mib@
```
#### Install Poetry
```pip3 install poetry```

#### Run Mib Server
```
poetry install
poetry run sc4snmp-mib-server
```