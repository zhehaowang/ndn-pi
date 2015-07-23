Change note for the new image (Updated Jul 22):
==========================

### Versions of tools on this image:

* ndn-cxx: [commit](https://github.com/named-data/ndn-cxx/commit/35020caedf296346332155e22eae447b7785b873), Jul 1, 2015 
* nfd: [commit](https://github.com/named-data/nfd/commit/2666473042796614a0c2a54636c29f5b17507470), Jun 26, 2015 (release 0.3.3)
* repo-ng: [commit](https://github.com/named-data/repo-ng/commit/6e818129190497de8851a6f2d0ae57dfcccb0f49), May 4, 2015 (latest)
* PyNDN2: [commit]((https://github.com/named-data/PyNDN2/commit/c67f23471c685ea6ab05c27b54c07544842e03fb), Jul 16, 2015 (latest)

### Recommended: 
* Use SD card > 4GB; 
* Expand the card to its actual size after writing the image; this can be done on Raspberry Pi using fdisk to redo the partition table, and then resize2fs. [instructions](http://raspberrypi.stackexchange.com/questions/499/how-can-i-resize-my-root-partition)

The image has little amount of free space left, which is likely to cause problems if testing as-is. (When testing as-is, experienced problems include a much higher chance of interest timeout, and data not received)

### Notes:
* /home/pi/ndn-pi: tracking https://github.com/zhehaowang/ndn-pi (origin), with https://github.com/named-data/ndn-pi (upstream); ndn-iot-start runs nfd-start, and registers / on udp multicast face.
* Libraries/binaries installed in default locations when compiling/installing from source; config files kept at default locations.
* User name: pi; password: raspberry; Network SSID: Raspi_NDN; Password: defaultpasswd;

### Changes:
* Base node constructor takes connectionInfo for creating face
* Added openloop publisher example (Requires specific configuration!)
* Updated library; (Change note being updated)
  * ConfigPolicyManager no longer takes IdentityStorage; [source](https://github.com/named-data/ndn-pi/blob/master/ndn_pi/security/iot_policy_manager.py#L62); correspondingly, we store the given identityStorage in IotPolicyManager.\_identityStorage
  * Import ThreadsafeFace from pyndn.threadsafe\_face instead; [source](https://github.com/named-data/ndn-pi/blob/master/ndn_pi/base_node.py#L25) and several occurrences
  * ThreadsafeFace stopWhen is removed; [source](https://github.com/named-data/ndn-pi/blob/master/ndn_pi/base_node.py#L142); every time isStopped is set to True, we call self.stop which contains self.loop.stop()
  * In the old version, public/private key pairs for identities are missing key-name-hash.pub file in .ndn/ndnsec-tmp-file; Generated another cert, and made it default for /home/controller; 
  * Make PyNDN encode the HMAC signature type, as Sha256WithRsa; (derived the modification from Adeola’s PyNDN) [source](https://github.com/named-data/PyNDN2/blob/master/python/pyndn/encoding/tlv_0_1_1_wire_format.py#L743-L744)
  * Copied getKeyType back to PyNDN’s basic\_identity\_storage (along with 7, it seems that public key TYPE is a deprecated concept?)
  * Removed public key type in iot\_manager’s PublicKey constructor. [source](https://github.com/named-data/ndn-pi/blob/master/ndn_pi/security/iot_identity_manager.py#L113-L115)
  * iot\_identity\_manager, when generating certificate for the added device, the IdentityCertificate constructor now takes a data packet, instead of just a name. [source](https://github.com/named-data/ndn-pi/blob/master/ndn_pi/security/iot_identity_manager.py#L124)
  * Use certificateCache\_ to store the root certificate, when root cert is downloaded (how we know/verify it’s root cert? Should the CA(controller)'s cert be preinstalled?) TODO: we should not install a downloaded cert into certificateCache, should populate certificateCache from ndnsec-public-info.db instead (Used to be Adeola's ID storage?).
  * Write public key to file system in iot\_private\_key\_storage, [source](https://github.com/named-data/ndn-pi/blob/master/ndn_pi/iot_node.py#L167) theoretically this could also be achieved if we override getPublicKey in iot\_private\_key\_storage, and tells that overridden function to look up the database for the public key
  * Store the signed certificate in certificateCache\_ on controller after receiving a valid certificate request. [source](https://github.com/named-data/ndn-pi/blob/master/ndn_pi/iot_controller.py#L249)
  * In PyNDN, cast int with str() when removing registered prefix [source](https://github.com/named-data/PyNDN2/blob/master/python/pyndn/node.py#L283)

zhehao@remap.ucla.edu
