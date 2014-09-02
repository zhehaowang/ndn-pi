
Named Data Network Internet of Things Toolkit (NDN-IOTT)
=======
Tutorial
=========

This tutorial will walk you through configuring and running your own IoT network over NDN.
Before following this tutorial, try running the led\_control example in <ndn-pi/examples>.

Copy the example folder to a new location so you can make changes.
 
Extending the LED control example
-------------------------------------

### Adding an LED node
The easiest way to extend the LED control network is to add another node that provides the
same LED service. To do that, load the configuration file for the simple LED node using

	    ndn-config led.conf

First, save the configuration to a new file, e.g. `led2.conf`, so that we don't override the
original settings for the LED node. Then, change the device name using the first option, 
'Edit network name settings'. You can choose any name you like. Once you are done editing the
device information, ndn-config will create and save network certificates for the new node.
You should not need to make any other changes to the configuration.    

Now you may run the new node, using

        sudo -E ./led_node.py led2.conf &

If you chose a different name for your new configuration, be sure to use that in place of `led2.conf`.    

If you run the new node and the original LED node on the same Raspberry Pi, you will see two 
entries in the viewer, but they will control the same LED. This 
is because both nodes are set up to use the same pin. If you set up another Raspberry Pi with 
an LED on pin 24, you will be able to control each LED separately.

You could also duplicate the viewer node, in order to view and control available LEDs from
another node.


### Adding commands to existing nodes

Another way to extend the network is to add more LEDs to the multi-LED node. Open
the configuration for the multi-LED node with

	    ndn-config led_multi.conf

Go to 'Edit command list' and look at the two defined commands. They are in the form

	    setLight/<pin number>

The multi-LED node contains logic that looks for pin numbers in commands on startup and
when a command interest is received. You may move LEDs by changing the pin number at the end
of the command, or add pins by adding a similar command. For example, to add an LED on pin 18,
add a new command with the following fields:    

	    Command name:  	setLight/18
	    Function name: 	onLightCommand
	    Keyword(s): led

Do not toggle signing/authorisation for now. Save the configuration file with the same name, and
re-run led\_multi.py. Don't forget to run the controller and viewer nodes if they are not already 
running.

### Adding authorization requirements

Named Data Networking allows for authenticated network interactions. This means that access to commands
can be restricted to nodes that have registered with the controller. By default, all IoT nodes request
certificates from the controller on startup, but they are not used unless another node requires signed 
commands.

In the example, the setLight commands do not require signing, meaning that anyone
 can turn the lights on or off, not just an IoT node in your network. We will now enforce signing for one of the 
LEDs in the multi-node. 

This part of the tutorial is best run across at least two Raspberry Pis, as running four nodes at once may overburden
the NDN forwarder on a single Pi.

First, we will make a copy of the viewer node configuration with a completely different network name.


Run 

        ndn-config viewer.conf

In 'Edit network name settings', change the 'Network prefix' to something else, such as 'otherhome'. Save this
as 'other\_viewer.conf'.  
You will also need to run a controller with the same network name, else the viewer node will not run at all.
To do this, you may run `ndn-config` with no arguments. Change the network name to match your new network prefix,
and make sure the controller and device name are the same. For example:

       Network prefix: otherhome
       Node name: controller
       Controller name: controller

Save this new configuration as  'other\_controller.conf'. 


Finally, we will turn on signing for one of the LEDs in the multi-LED node. Run

        ndn-config led_multi.conf

Go to 'Edit command list' and edit one of the commands. Use the 'Toggle signed' button to make the command signed.
 Save this configuration under a new name, such as 'led_multi_signed.conf'.

Now, make sure at least the following nodes are running in your network:

    *  Default controller (`python -m ndn_pi.iot_controller`)
    *  Modified multi-LED node (`sudo -E python led_multi_node.py led_multi_signed.conf`)
    *  Other controller (`python -m ndn_pi.iot_controller other_controller.conf`)
    *  Modified viewer (`python viewer.py other_viewer.conf`)

Now try to turn the LEDs on and off. You will find