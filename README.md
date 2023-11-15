# DependencyConfusion-checker
Checking dependency confusion for npm packages in public registry. 

The tool written in python is checking dependency confusion for npm packages in public registry. It is useful in finding the dependency
confusion attacks which even leads to RCE. 

To use this provide the package.json file url , if you get 200 then it's not vulnerable , if you other http response then it may be vulnerable.
