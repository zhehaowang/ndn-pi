# Copyright (C) 2014 Regents of the University of California.
# Author: Spencer Sutterlin <ssutterlin1@ucla.edu>
# 
# This file is part of ndn-pi (Named Data Networking - Pi).
#
# ndn-pi is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# A copy of the GNU General Public License is in the file COPYING.

from 2-publisher-command-interest.publish_pir import PirDataLogger

# TODO: don't hardcode, instead get from command interest
nodeType = "pir"

def onDataGWInit(interest, data):
    pass
    # verify data is signed by barcode
    # install as root of trust
    data.getContent()
    # How? Where? There's no repo running on these guys, do we just save to disk or use ndn-cxx ndnsec tools?
    # ndnsec-cert-install

def onTimeout(interest):
    pass
    # resend interest once or twice?

# Some of these function args are probably not necessary
def onInterest(prefix, interest, transport, registeredPrefixId):
    # if interest.getName() matches "/home/dev/<serial>/<auth>"
        # do we have to verify interest signature?
        data = Data(Name("/home/dev/<serial>/<auth>"))
        data.setContent(public key)
        # send data
        interest = Interest(Name("/home/gw").append(<auth>))
        # sign interest by barcode
        face.expressInterest(interest, onDataGWInit, onTimeout)

def onRegisterFailed(prefix):
    pass
    # try, try again

# check for self keys
# if not keys, generate key for self
prefix = Name("/home/dev").append(serial)
face.registerPrefix(prefix, onInterest, onRegisterFailed)

# listen for <prefix> (will come from gateway)

# listen for <prefix>/command/pir/on or <prefix>/command/cec/off, etc.
if nodeType == "pir":
    logger = PirDataLogger(data_interval = 0.5) # sample at every 0.5 seconds (also affects face.processEvents)
    logger.run()
elif nodeType == "cec":
    # TODO: implement
    print "CEC stuff"