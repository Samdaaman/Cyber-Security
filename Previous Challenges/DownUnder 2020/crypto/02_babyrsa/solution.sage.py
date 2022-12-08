

# This file was *autogenerated* from the file solution.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1024 = Integer(1024); _sage_const_0x10001 = Integer(0x10001); _sage_const_557 = Integer(557); _sage_const_127 = Integer(127); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_19574201286059123715221634877085223155972629451020572575626246458715199192950082143183900970133840359007922584516900405154928253156404028820410452946729670930374022025730036806358075325420793866358986719444785030579682635785758091517397518826225327945861556948820837789390500920096562699893770094581497500786817915616026940285194220703907757879335069896978124429681515117633335502362832425521219599726902327020044791308869970455616185847823063474157292399830070541968662959133724209945293515201291844650765335146840662879479678554559446535460674863857818111377905454946004143554616401168150446865964806314366426743287 = Integer(19574201286059123715221634877085223155972629451020572575626246458715199192950082143183900970133840359007922584516900405154928253156404028820410452946729670930374022025730036806358075325420793866358986719444785030579682635785758091517397518826225327945861556948820837789390500920096562699893770094581497500786817915616026940285194220703907757879335069896978124429681515117633335502362832425521219599726902327020044791308869970455616185847823063474157292399830070541968662959133724209945293515201291844650765335146840662879479678554559446535460674863857818111377905454946004143554616401168150446865964806314366426743287); _sage_const_3737620488571314497417090205346622993399153545806108327860889306394326129600175543006901543011761797780057015381834670602598536525041405700999041351402341132165944655025231947620944792759658373970849932332556577226700342906965939940429619291540238435218958655907376220308160747457826709661045146370045811481759205791264522144828795638865497066922857401596416747229446467493237762035398880278951440472613839314827303657990772981353235597563642315346949041540358444800649606802434227470946957679458305736479634459353072326033223392515898946323827442647800803732869832414039987483103532294736136051838693397106408367097 = Integer(3737620488571314497417090205346622993399153545806108327860889306394326129600175543006901543011761797780057015381834670602598536525041405700999041351402341132165944655025231947620944792759658373970849932332556577226700342906965939940429619291540238435218958655907376220308160747457826709661045146370045811481759205791264522144828795638865497066922857401596416747229446467493237762035398880278951440472613839314827303657990772981353235597563642315346949041540358444800649606802434227470946957679458305736479634459353072326033223392515898946323827442647800803732869832414039987483103532294736136051838693397106408367097); _sage_const_7000985606009752754441861235720582603834733127613290649448336518379922443691108836896703766316713029530466877153379023499681743990770084864966350162010821232666205770785101148479008355351759336287346355856788865821108805833681682634789677829987433936120195058542722765744907964994170091794684838166789470509159170062184723590372521926736663314174035152108646055156814533872908850156061945944033275433799625360972646646526892622394837096683592886825828549172814967424419459087181683325453243145295797505798955661717556202215878246001989162198550055315405304235478244266317677075034414773911739900576226293775140327580 = Integer(7000985606009752754441861235720582603834733127613290649448336518379922443691108836896703766316713029530466877153379023499681743990770084864966350162010821232666205770785101148479008355351759336287346355856788865821108805833681682634789677829987433936120195058542722765744907964994170091794684838166789470509159170062184723590372521926736663314174035152108646055156814533872908850156061945944033275433799625360972646646526892622394837096683592886825828549172814967424419459087181683325453243145295797505798955661717556202215878246001989162198550055315405304235478244266317677075034414773911739900576226293775140327580)
from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
from sage.all import *
from icecream import ic

def test():
    p, q = getPrime(_sage_const_1024 ), getPrime(_sage_const_1024 )
    n = p*q
    e = _sage_const_0x10001 

    s = pow(_sage_const_557 *p - _sage_const_127 *q, n - p - q, n)
    s_inv = pow(s, -_sage_const_1 , n)

    assert (_sage_const_557 *p - _sage_const_127 *q) == s_inv

    # solve 557*p^2 - s_inv*p - 127*n = 0
    x = var('x')
    f = _sage_const_557 *x**_sage_const_2  - int(s_inv)*x - _sage_const_127 *n
    sols = [i.rhs() for i in solve(f, x)]
    ic(sols)
    p_test = sols[_sage_const_0 ] if sols[_sage_const_0 ] > _sage_const_0  else sols[_sage_const_1 ]
    ic(p_test)
    assert p_test == p


def solution():
    n = _sage_const_19574201286059123715221634877085223155972629451020572575626246458715199192950082143183900970133840359007922584516900405154928253156404028820410452946729670930374022025730036806358075325420793866358986719444785030579682635785758091517397518826225327945861556948820837789390500920096562699893770094581497500786817915616026940285194220703907757879335069896978124429681515117633335502362832425521219599726902327020044791308869970455616185847823063474157292399830070541968662959133724209945293515201291844650765335146840662879479678554559446535460674863857818111377905454946004143554616401168150446865964806314366426743287 
    s = _sage_const_3737620488571314497417090205346622993399153545806108327860889306394326129600175543006901543011761797780057015381834670602598536525041405700999041351402341132165944655025231947620944792759658373970849932332556577226700342906965939940429619291540238435218958655907376220308160747457826709661045146370045811481759205791264522144828795638865497066922857401596416747229446467493237762035398880278951440472613839314827303657990772981353235597563642315346949041540358444800649606802434227470946957679458305736479634459353072326033223392515898946323827442647800803732869832414039987483103532294736136051838693397106408367097 
    c = _sage_const_7000985606009752754441861235720582603834733127613290649448336518379922443691108836896703766316713029530466877153379023499681743990770084864966350162010821232666205770785101148479008355351759336287346355856788865821108805833681682634789677829987433936120195058542722765744907964994170091794684838166789470509159170062184723590372521926736663314174035152108646055156814533872908850156061945944033275433799625360972646646526892622394837096683592886825828549172814967424419459087181683325453243145295797505798955661717556202215878246001989162198550055315405304235478244266317677075034414773911739900576226293775140327580 
    e = _sage_const_0x10001 

    s_inv = pow(s, -_sage_const_1 , n)
    # solve 557*p^2 - s_inv*p - 127*n = 0
    x = var('x')
    f = _sage_const_557 *x**_sage_const_2  - int(s_inv)*x - _sage_const_127 *n
    sols = [i.rhs() for i in solve(f, x)]
    p = int(sols[_sage_const_0 ] if sols[_sage_const_0 ] > _sage_const_0  else sols[_sage_const_1 ])
    q = n // p
    assert n == p*q

    lam = (p-_sage_const_1 )*(q-_sage_const_1 )
    d = pow(e, -_sage_const_1 , lam)
    ptl = pow(c, d, n)
    pt = long_to_bytes(ptl)
    ic(pt)


if __name__ == '__main__':
    solution()
