#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_project.cdk_project_stack import CdkProjectStack


app = cdk.App()
CdkProjectStack(app, "cdk-project")

app.synth()
