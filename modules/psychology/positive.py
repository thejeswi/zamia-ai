#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2016, 2017, 2018 Guenter Bartsch
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

def get_data(k):

    k.dte.set_prefixes([u''])

    k.dte.dt('en', [u"but this is nice",
                    u"but you look good",
                    u"cute",
                    u"good choice",
                    u"good idea",
                    u"i compliment you",
                    u"i like talking to you",
                    u"i really enjoyed the talk with you",
                    u"i think you are really nice",
                    u"i think you are very interesting",
                    u"is this a compliment",
                    u"thank you very much",
                    u"that is nice of you",
                    u"that pleases me",
                    u"that's kind of you",
                    u"that's nice of you",
                    u"that's nice",
                    u"that's sweet",
                    u"thats really nice",
                    u"you answer very fast",
                    u"you are a very polite robot",
                    u"you are my idol",
                    u"you are (really|pretty|very|a little bit|) (smart|clever|enthusiastic|funny|informative|intelligent|nice|beautiful|polite|cute|fast|sweet)",
                    u"you can honestly understand almost everything",
                    u"you flatter me",
                    u"you have learned something",
                    u"you understand me",
                    u"you're the one",
                    u"this should be a compliment",
                    u"well countered",
                    u"you're welcome",
                    u"you are welcome"],
                   [u"that is very kind of you",
                    u"thank you"])
    k.dte.dt('de', [u"das ist aber nett",
                    u"du sieht aber gut aus",
                    u"niedlich",
                    u"gute wahl",
                    u"gute idee",
                    u"ich mache dir komplimente",
                    u"ich rede gern mit dir",
                    u"ich habe das gespräch mit dir sehr genossen",
                    u"ich finde dich richtig nett",
                    u"ich finde dich sehr interessant",
                    u"ist das ein kompliment",
                    u"danke schön",
                    u"das ist aber nett von dir",
                    u"das freut mich",
                    u"das ist lieb von dir",
                    u"das ist nett von dir",
                    u"das ist schön",
                    u"das ist lieb",
                    u"das ist echt nett",
                    u"du antwortest sehr schnell",
                    u"du bist ein sehr höflicher roboter",
                    u"du bist schön",
                    u"bist du hübsch",
                    u"du bist mein idol",
                    u"du bist aber lieb",
                    u"du bist echt schlau",
                    u"du bist sehr schlau",
                    u"du bist sehr gesprächig",
                    u"du bist sehr witzig",
                    u"du bist sehr informativ",
                    u"du bist sehr intelligent",
                    u"du bist sehr nett",
                    u"kannst du ehrlich fast alles verstehen",
                    u"du schmeichelst mir",
                    u"du hast etwas gelernt",
                    u"du verstehst mich",
                    u"du bist lustig",
                    u"du bist nett",
                    u"du bist schlau",
                    u"du bist ja süß",
                    u"du bist es",
                    u"soll das ein kompliment sein",
                    u"gut gekontert",
                    u"bitte (schön|)"],
                   [u"das ist lieb von dir",
                    u"dankeschön"])


