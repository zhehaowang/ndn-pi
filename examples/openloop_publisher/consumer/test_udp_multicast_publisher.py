# -*- Mode:python; c-file-style:"gnu"; indent-tabs-mode:nil -*- */
#
# Copyright (C) 2014-2015 Regents of the University of California.
# Author: Jeff Thompson <jefft0@remap.ucla.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# A copy of the GNU Lesser General Public License is in the file COPYING.

import time

# remove Adeola's version of PyNDN in sys.path
# this would also require
# export PYTHONPATH=$PYTHONPATH:~/zhehao-test/pyndn2/python

# this test does not expect prefix registered on the remote nfd that we connect to...
import sys
if ("/usr/local/lib/python2.7/dist-packages/PyNDN-2.0a3-py2.7.egg" in sys.path):
    sys.path.remove("/usr/local/lib/python2.7/dist-packages/PyNDN-2.0a3-py2.7.egg")

from pyndn import Name
from pyndn import Data
from pyndn import Face
from pyndn.security import KeyChain

from pyndn.transport.udp_transport import UdpTransport

def dump(*list):
    result = ""
    for element in list:
        result += (element if type(element) is str else repr(element)) + " "
    print(result)

class Echo(object):
    def __init__(self, keyChain, certificateName):
        self._keyChain = keyChain
        self._certificateName = certificateName
        self._responseCount = 0
        self._sentCount = 0

    def onInterest(self, prefix, interest, face, interestFilterId, filter):
        self._responseCount += 1

        # Make and sign a Data packet.
        data = Data(interest.getName())
        content = "Echo " + interest.getName().toUri()
        data.setContent(content)
        self._keyChain.sign(data, self._certificateName)

        dump("Sent content", content)
        face.putData(data)

    def onRegisterFailed(self, prefix):
        self._responseCount += 1
        dump("Register failed for prefix", prefix.toUri())
    
    def putData(self, face, name, content):
        dataContent = content
        self._sentCount += 1
        data = Data(name)
        data.setContent(dataContent + str(self._sentCount))
        self._keyChain.sign(data, self._certificateName)
        dump("Sent content: " + data.getName().toUri())
        face.putData(data)
        #transport.send(data.wireEncode().buf())

def main():
    # The default Face will connect using a Unix socket, or to "localhost".
    transport = UdpTransport()
    # TODO: This multicast address should read from nfd configuration
    conn = UdpTransport.ConnectionInfo("224.0.23.170")
    face = Face(transport, conn)
    #face = Face()
    
    # Use the system default key chain and certificate name to sign commands.
    keyChain = KeyChain()
    face.setCommandSigningInfo(keyChain, keyChain.getDefaultCertificateName())

    # Also use the default certificate name to sign data packets.
    echo = Echo(keyChain, keyChain.getDefaultCertificateName())
    prefix = Name("/testecho")
    dump("Register prefix", prefix.toUri())
    face.registerPrefix(prefix, echo.onInterest, echo.onRegisterFailed)
    # Though a remore registration would fail, not including this would still cause _socket None in transport.

    while True:
        echo.putData(face, Name("/home/udp-test1").append(str(int(time.time() * 1000))), "test")
        face.processEvents()
        # We need to sleep for a few milliseconds so we don't use 100% of the CPU.
        time.sleep(1)

    face.shutdown()

main()
