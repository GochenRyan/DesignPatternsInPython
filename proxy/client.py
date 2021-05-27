# -*- coding: utf-8 -*-

import schoolgirl
import proxy

if __name__ == '__main__':
    oGirl = schoolgirl.CSchoolGirl("翠花")
    oProxy = proxy.CProxy(oGirl)
    oProxy.GiveFlowers()