#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2014 Marcus Müller.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from iosig_wise import iosig_wise
class qa_iosig_wise (gr_unittest.TestCase):
    def setUp (self):
        pass
        #self.tb = gr.top_block ()

    def tearDown (self):
        pass
        #self.tb = None

    def test_001_t (self):
        def sig_cmp(a,b):
            return ( a.min_streams() == b.min_streams() and\
                     a.max_streams() == b.max_streams() and\
                     a.sizeof_stream_items() == b.sizeof_stream_items() )
        # set up fg
        for in_min in range(24):
            for t in (gr.sizeof_float, gr.sizeof_gr_complex):
                in_sig = gr.io_signature(in_min,in_min,t) 
                out_sig = gr.io_signature(23-in_min, 23-in_min, t)
                block_under_test = iosig_wise(in_sig,out_sig)
                self.assert_(sig_cmp(block_under_test.input_signature(), in_sig), "input does not match")
                self.assert_(sig_cmp(block_under_test.output_signature(), out_sig), "output does not match")

if __name__ == '__main__':
    gr_unittest.run(qa_iosig_wise, "qa_iosig_wise.xml")
