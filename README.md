# webhooks
github code(app + Dockerfile) -----------trigger(via webhook)------>openshift deployment---->user

no. commit == no. builds
***********************************************************************************************************************************
public url 

public dns + build config + genric secrets key  
************************************************************************************************************************************
if we dont add --statergy option then we add mention specific path of python file do based on that openshift system autoamtin find the image that is need to run python code.
Due to we added --statergy=docker openshift will first start building and image then save to local repo then run the container
