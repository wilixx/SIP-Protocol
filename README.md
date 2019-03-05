![Downloads](https://img.shields.io/github/downloads/trishantpahwa/SIP-Protocol/total.svg?style=popout)

# Session-Initiation-Protocol
A signaling protocol used for initiating, maintaining and terminating real-time sessions that include voice, video and messaging applications.

#### The protocol was invented and designed by J. Rosenberg. And as mentioned in the [RFC 3261](https://www.ietf.org/rfc/rfc3261.txt)
#### To refer more about the basic workflow of the protocol is mentioned in the [RFC 3265](https://www.ietf.org/rfc/rfc3265.txt) 

## The following diagrams showcase the working of SIP Protocol:
### Client Registeration to Registerar
![Registeration of Client to Registerar](https://raw.githubusercontent.com/trishantpahwa/SIP-Protocol/master/images/SIP-registration-flow.png)
### Communication between Client and Registerar to request for transferring media from one client to another
![Work flow of Client and B2BUA](https://raw.githubusercontent.com/trishantpahwa/SIP-Protocol/master/images/SIP-B2BUA-call-flow.png)
### Flow Diagram to showcase the working of SIP
![Basic flow](https://raw.githubusercontent.com/trishantpahwa/SIP-Protocol/master/images/SIP_signaling.png)

I also added a few extra functionalities such as Deregisteration of client 
that could improve the working of the protocol.

The project contains a Node(Client), a Registerar(Server).
Multiple nodes can connect to the registerar and communicate with each other.
The project uses a streaming algorithm that I studied about in my University 
in my Senior Year.

### Developed this project under the guidence of Mr. Anil and the Research and Development Team at [Vaaan Infra Pvt Ltd](http://VaaanInfra.com).
