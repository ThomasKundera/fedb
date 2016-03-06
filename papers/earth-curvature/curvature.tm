<TeXmacs|1.99.2>

<style|article>

<\body>
  <\doc-data|<doc-title|Observing Earth ``curvature''>|<doc-author|<\author-data|<author-name|TK>>
    \;
  <|author-data>
    \;
  <|author-data>
    \;
  </author-data>>>
    \;
  </doc-data>

  <section|Presentation of the problem>

  <subsection|Flatters point of view>

  <big-figure|<image|figures/flat-earth-horizon-flat.jpg|12cm|8cm||>|<label|figflatflat>(from
  a flatter post)>

  Very often, Flat-Earth (FE) propagandists (referred after as ``flatters'')
  will show pictures like Figure <reference|figflatflat> and claim ``as you
  can see, the horizon is flat, so the Earth can't be round''.

  But what they expect to see and how the ``curve'' should look like is a bit
  confuse for them.

  <subsection|What some expects and why it doesnt have much meaning>

  <big-figure|<image|figures/STS106-702-78_350.jpg|350px|216px||>|<label|figspacecurve>(Credit
  NASA)>

  Flatters are looking for something like Figure <reference|figspacecurve>
  but at very low (less than <math|2 m>) to moderate (<math|10-30 km>)
  altitude.

  But of course, it make little sense: what should that ``curvature'' become
  when looking a bit on side ? If the highest point moves with the eyes of
  the observer, then it's obviously a geometric abheration, not a real
  curvature.

  So the question is obviously not well asked by flatters, but then, what
  should it be?

  <subsection|The questions we'll try to answer>

  How to see the curvature of Earth?

  Why can't we see it at ground level and what should we expect as we reach
  an higher altitude? From which altitude should we be able to see a
  difference with a FE model, and how?

  <section|Our tools>

  <subsection|Mathematics>

  Basic \ geometry, in both 2D and 3D will be needed.

  <subsection|Povray>

  The open-source Povray \ renderer will be used to illustrates some points
  when needed. Three reasons justified this choice:

  <\itemize-dot>
    <item>It's very well adapted o mathematics object rendering (a sphere is
    a sphere, not a polygon mesh with some ``curves'' in it added),

    <item>Being a script language it's easy to foolproof, transmit the source
    code and discuss bugs and improvements,

    <item>Being open-source anyone can try and check its output,

    <item>I know it a bit.
  </itemize-dot>

  <subsection|Data>

  <subsection|Globe model>

  The globe will in first approximation be modeled by a perfect sphere of
  6371 km radius, floating in an empty space.

  In Povray, its surface will be represented by just a simple modeled water.
  Some (very simple) clouds model (a 2D layer at about 3 km above surface)
  will be used in some image as well as a round atmospheric layer around with
  ***.

  <subsection|Flat Earth model>

  The Flat Earth model will be represented by a flat cylinder of 10000 km in
  radius (measured distance from north to south pole) and an illustrative
  thickness of 100km floating in an empty space.

  In Povray, its flat top surface will be covered with the same simple
  modeled water, the rest being a uniform braun color. Some (very simple)
  clouds model (a 2D layer at about 3 km above surface) will be used in some
  image as well as a flat atmospheric layer.\ 

  <section|Disappearance beyond the horizon><label|SectVanishing>

  <subsection|Generalities>

  As a ship is leaving the shore, or when looking at a distant island, the
  question can be ``how far can I see a remote object?''. This will be
  computed in this section.

  On a flat Earth, the horizon should be pushed to infinity, meaning that
  objects could be seen at arbitrary distance in good weather conditions.
  Something that everyday observation contradict. One never saw the coast of
  Englands from New-York.

  <subsection|Computation>

  <subsubsection|A bit of math>

  <big-figure|<image|code/eukleides/distance-of-sigh.eps|6cm|||>|<label|figmathorizon>>

  The general idea of the situation is given on Figure <label|figmathorizon>:
  an observer, at location <math|A<rprime|'>>, standing above sea level at an
  height <math|h<rsub|a>> is looking at a distant object located at
  <math|B<rprime|'>> and a height <math|h<rsub|b>>. We want to compute the
  distance <math|d=d<rsub|a>+d<rsub|b>>, being the maximum distance at which
  those objects can be seen despite of the curvature of the Earth.

  The problem is mathematically trivial once noted that <math|A<rprime|'>OC>
  and <math|B<rprime|'>OC> are right triangles in C. So that we can just
  write the Pytagore theorem in them:

  <\equation*>
    OA<rprime|'><rsup|2>=OC<rsup|2>+A<rprime|'>C<rsup|2>
  </equation*>

  and:

  <\equation*>
    OB<rprime|'><rsup|2>=OC<rsup|2>+B<rprime|'>C<rsup|2>
  </equation*>

  The first one can be rewrote as:

  <\eqnarray*>
    <tformat|<table|<row|<cell|<around*|(|r+h<rsub|a>|)><rsup|2>>|<cell|=>|<cell|r<rsup|2>+d<rsup|2><rsub|a>>>|<row|<cell|r<rsup|2>+h<rsup|2><rsub|a>+2rh<rsub|a>>|<cell|=>|<cell|r<rsup|2>+d<rsup|2><rsub|a>>>|<row|<cell|h<rsup|2><rsub|a>+2rh<rsub|a>>|<cell|>|<cell|=d<rsup|2><rsub|a>>>>>
  </eqnarray*>

  And so:

  <\equation*>
    d<rsub|a>=<sqrt|h<rsup|2><rsub|a>+2rh<rsub|a>><label|eqda>
  </equation*>

  and the same for <math|d<rsub|b>>:

  <\equation*>
    d<rsub|b>=<sqrt|h<rsup|2><rsub|b>+2rh<rsub|b>>
  </equation*>

  So, summing he two, the maximum distance at which an object of height
  <math|h<rsub|b>> seen from ah height <math|h<rsub|a>> is:

  <\equation>
    d<rsub|>=<sqrt|h<rsup|2><rsub|a>+2rh<rsub|a>>+<sqrt|h<rsup|2><rsub|b>+2rh<rsub|b>><label|eqd>
  </equation>

  <subsubsection|Note about what we call distance between two points on
  Earth>

  The computed value <math|d=d<rsub|a>+d<rsub|b>> is not exactly what we
  would measure on Earth, as we would measure the distance from
  <math|A<rprime|'>> to <math|B<rprime|'>> following the curve, so the arc
  <math|<wide|AB|\<invbreve\>>>. For small distances it doesnt change much,
  but if become highly irrelevant for large ones. FIXME: numerical values
  would be cool.

  <subsection|Numeric values>

  <subsubsection|First example and a useful remark>

  Knowing that <math|r=6371000 m> and supposing I'm standing on a beach
  looking at the sea, my eyes at an height of about <math|h<rsub|a>=2 m>, the
  horizon lies for me at <math|d<rsub|a>=5050 m>, so about <math|5 km>. And
  many flatters would only look at that distance <math|d<rsub|a>>, being the
  distance to horizon, and confuse it with the largest distance something can
  be observed. But if only I want to know if I can wave at someone else away
  at the same height that I am, the distance is doubled, becoming more than
  <math|10 km>.

  <subsubsection|Graphes>

  Starting from Equation (<reference|eqd>), we can rewrite:

  <\eqnarray*>
    <tformat|<table|<row|<cell|d<rsub|>>|<cell|=>|<cell|<sqrt|h<rsup|2><rsub|a>+2rh<rsub|a>>+<sqrt|h<rsup|2><rsub|b>+2rh<rsub|b>>>>|<row|<cell|<sqrt|h<rsup|2><rsub|b>+2rh<rsub|b>>>|<cell|=>|<cell|d-<sqrt|h<rsup|2><rsub|a>+2rh<rsub|a>>>>|<row|<cell|h<rsup|2><rsub|b>+2rh<rsub|b>>|<cell|=>|<cell|<around*|(|d-<sqrt|h<rsup|2><rsub|a>+2rh<rsub|a>>|)><rsup|2>>>>>
  </eqnarray*>

  For sake of simplicity lets name <math|K=d-<sqrt|h<rsup|2><rsub|a>+2rh<rsub|a>>>

  <\eqnarray*>
    <tformat|<table|<row|<cell|h<rsup|2><rsub|b>+2rh<rsub|b>>|<cell|=>|<cell|K<rsup|2>>>|<row|<cell|h<rsup|2><rsub|b>+2rh<rsub|b>-K<rsup|2>>|<cell|=>|<cell|0<label|eq2><eq-number>>>>>
  </eqnarray*>

  Equation (<reference|eq2>) is just a second degree equation with
  <math|h<rsub|b>> as variable. So lets set
  <math|\<Delta\>=4r<rsup|2>+4K<rsup|2>>, and we have the only positive
  solution:

  <\equation*>
    h<rsub|b>=<frac|-2r+<sqrt|\<Delta\>>|2>
  </equation*>

  <math|h<rsub|b>> is the lowest object that would be seen at distance d from
  height <math|h<rsub|a>>.

  A few plots are displayed of Figure <reference|fighorizonplot>. Even from
  ground level, anything height than <math|1000 m> can be seen from as much
  as <math|100 km> of distance. And if we climb at moderate altitude of
  <math|250 m>, then mounts even lower that this can be seen from that
  distance. In a common case where we would be on a small mountain at about
  <math|1000 m> of altitude, a similar peak could be seen at more than
  <math|200 km> away.

  As one can see, there is no surprise in many reported observations and
  pictures that flatters takes for a ``proof'' that the Earth could not be
  round.

  <\big-figure>
    <image|code/gnuplot/distances.eps|12cm|||>
  </big-figure|<label|fighorizonplot>>

  <subsection|A note about looming and mirages>

  <big-figure|<image|figures/Looming_with_towering_and_mirage_of_Farallon_Islands.jpg|12cm|10cm||>|Example
  of mirage and looming (credit : Wikipedia<cite|BibWikiLoomingwiki:Looming>)>

  In some weather conditions, the light rays can be deflected quite a lot by
  the index gradient of air at different temperature.

  <subsection|When observing, be precise>

  <\itemize-dot>
    <item>Very precise location and altitude of both observing and observed
    point (usually not mentioned by flatters)

    <item>mirages: is the observation ``exceptional'' in the sense that the
    day after (or even one hour after) the object cannot be seen? Is it
    during a very warm day or a temperature inversion? Avoid hot days, and
    conditions when the sea is a lot colder than the above air. Flatters will
    usually mention one exceptional observation, forgetting about all the
    usual case when it doesnt happens.
  </itemize-dot>

  <section|Height of the horizon>

  <subsection|Presentation of the problem>

  When going up in altitude, the horizon is lowering due to the fact that the
  Earth has a finite spherical surface.

  The effect is rather small, as it will be shown.

  The lowering of horizon for a FE model is a bit more tricky to compute
  (there are several incompatibles - and implausible - FE models). Most FE
  propagandist believes the horizon to always stay at ``eye-level''.

  <subsection|Computation>

  <big-figure|<image|code/eukleides/low-horizon.eps|10cm|11cm||>|>

  The distance <math|d<rsub|a>> has already been computed in Equation
  (<reference|eqda>), <math|d<rsub|a>=<sqrt|h<rsup|2>+2rh>>.

  In triangle <math|A<rprime|'>BB<rprime|'>> we have:

  <\eqnarray*>
    <tformat|<table|<row|<cell|d<rsup|><rprime|'><rsup|2>>|<cell|=>|<cell|d<rsup|2><rsub|b>+d<rsup|2><rsub|a>>>|<row|<cell|d<rprime|'><rsup|2>>|<cell|=>|<cell|d<rsup|2><rsub|b>+h<rsup|2>+2rh>>>>
  </eqnarray*>

  In triangle <math|OA<rprime|'>B<rprime|'>> we have:<math|>

  <\eqnarray*>
    <tformat|<table|<row|<cell|<around*|(|r+d<rsub|b>|)><rsup|2>>|<cell|=>|<cell|d<rprime|'><rsup|2>+<around*|(|r+h<rsub|>|)><rsup|2>>>|<row|<cell|r<rsup|2>+d<rsup|2><rsub|b<rsup|>>+2rd<rsub|b>>|<cell|=>|<cell|d<rprime|'><rsup|2>+r<rsup|2>+h<rsup|2>+2rh>>|<row|<cell|d<rsub|b><rsup|2>+2rd<rsub|b><rsub|>>|<cell|=>|<cell|d<rprime|'><rsup|2>+h<rsup|2>+2rh>>|<row|<cell|2rd<rsub|b>>|<cell|=>|<cell|h<rsup|2>+2rh+h<rsup|2>+2rh>>|<row|<cell|2rd<rsub|b>>|<cell|=>|<cell|2h<rsup|2>+4rh>>|<row|<cell|d<rsub|b>>|<cell|=>|<cell|<around*|(|h<rsup|2>+2rh|)>/r<eq-number><label|eqdb>>>>>
  </eqnarray*>

  What we are interested in is the angle <math|\<alpha\>=<wide|BA<rprime|'>B<rprime|'>|^>>.

  <\eqnarray*>
    <tformat|<table|<row|<cell|<math-up|tan><around*|(|\<alpha\>|)>>|<cell|=>|<cell|d<rsub|b>/d<rsub|a>>>|<row|<cell|<math-up|tan><around*|(|\<alpha\>|)>>|<cell|=>|<cell|<frac|h<rsup|2>+2rh|r<sqrt|h<rsup|2>+2rh>>>>|<row|<cell|\<alpha\>>|<cell|=>|<cell|<math-up|atan><around*|(|<frac|<sqrt|h<rsup|2>+2rh>|r>|)><eq-number><label|eqata>>>>>
  </eqnarray*>

  <subsection|Numerical values>

  <big-figure|<image|code/gnuplot/angle_horizon.eps|12cm|||>|<label|figatana>>

  On Figure <reference|figatana>, is plotted the value of angle
  <math|\<alpha\>> in function of the altitude in kilometers. At <math|10 km>
  of altitude, the angle is about 3<degreesign>, an unnoticeable value
  without tools. one has to reach about <math|100 km> to see a clearly
  noticeable deviation of 10<degreesign> from the ground.

  So anyone expecting to see something significant at a lower altitude is
  misleaded.

  <subsection|A note about ``8 inches per miles squared''>

  A common value used by flatters to compute distance to horizon is ``8
  inches per miles squared''. That formulation cant be correct (it's even no
  dimensionaly coherent), but it may give an numerical approximation of the
  correct value in some conditions.

  <big-figure|<image|code/eukleides/eight-inches.eps|8cm|||>|<label|FigEigthInches>>

  It is first important to recall that if one wants to know from how long an
  object will be visible, the correct method is described in Section
  <reference|SectVanishing>, not here. The computation done here is only able
  to measure some ``drop''.

  There are at least two ways to consider a ``drop''. As seen in Figure
  <inactive|<reference|FigEightInches>>, the ``drop'' can either be
  <math|h<rprime|'>> (the distance to ground on a local verical) or
  <math|h<rprime|''>> (distance to ground according to a line normal to the
  horizontal at <math|A>). The distance can also be computed two ways: either
  <math|d> being the distance in straight line betwen <math|A> and <math|B>,
  or, by the arc <math|<wide|AB<rprime|'>|\<invbreve\>>> or
  <math|<wide|AB<rprime|''>|\<invbreve\>>>, which would be the value given by
  any measure on a map.

  This gives us four method to compute that ``drop'' (local or remote verical
  and straight line or arc) plus the ``eight inches'' one.

  <subsubsection|Computing <math|h<rprime|'>>>

  In triangle OAB:

  <\eqnarray*>
    <tformat|<table|<row|<cell|OA<rsup|2>+AB<rsup|2>>|<cell|=>|<cell|OB<rsup|2>>>|<row|<cell|r<rsup|2>+d<rsup|2>>|<cell|=>|<cell|<around*|(|r+h<rprime|'>|)><rsup|2>>>|<row|<cell|r<rsup|2>+d<rsup|2>>|<cell|=>|<cell|r<rsup|2>+h<rprime|'><rsup|2>+2rh<rprime|'>>>|<row|<cell|h<rprime|'><rsup|2>+2rh<rprime|'>-d<rsup|2>>|<cell|=>|<cell|0>>>>
  </eqnarray*>

  We consider the positive solution of the above equation:

  <\equation*>
    h<rprime|'>=<sqrt|r<rsup|2>+d<rsup|2>>-r
  </equation*>

  <subsubsection|Computing length of arc \ <math|<wide|AB<rprime|'>|\<invbreve\>>>>

  What we are interested in is the angle <math|\<alpha\>=<wide|AOB<rprime|'>|^>>.

  <\eqnarray*>
    <tformat|<table|<row|<cell|<math-up|tan><around*|(|\<alpha\>|)>>|<cell|=>|<cell|d<rsub|>/r>>|<row|<cell|\<alpha\>>|<cell|=>|<cell|<math-up|atan><around*|(|<frac|d|r>|)>>>>>
  </eqnarray*>

  <math|<wide|AB<rprime|'>|\<invbreve\>>=l<rprime|'>=atan<around*|(|d/r|)>r>

  <\math>
    atan<around*|(|d/r|)>=l<rprime|'>/r

    d=r tan<around*|(|l<rprime|'>/r|)>
  </math>

  <subsubsection|Computing <math|h<rprime|''>>>

  The triangle <math|B B<rprime|'> B<rprime|''>> is isomorph to triange
  <math|O A B>. Which means:

  <math|<choice|<tformat|<table|<row|<cell|h<rprime|'><rsup|2>+l<rsup|2>=h<rprime|''><rsup|2>>>|<row|<cell|d/r=l/h<rprime|'>>>>>>\<Rightarrow\>h<rprime|'><rsup|2>+<around*|(|<frac|dh<rprime|'>|r>|)><rsup|2>=h<rprime|''><rsup|2>>

  <\eqnarray*>
    <tformat|<table|<row|<cell|h<rprime|''><rsup|2>>|<cell|=>|<cell|<frac|d<rsup|2>h<rprime|'><rsup|2>|r<rsup|2>>+h<rprime|'><rsup|2>>>|<row|<cell|h<rprime|''>>|<cell|=>|<cell|<sqrt|<frac|d<rsup|2>h<rprime|'><rsup|2>|r<rsup|2>>+h<rprime|'><rsup|2>>>>>>
  </eqnarray*>

  <subsubsection|Computing length of arc \ <math|<wide|AB<rprime|''>|\<invbreve\>>>>

  What we are interested in is the angle <math|\<alpha\>=<wide|AOB<rprime|''>|^>>.

  <\eqnarray*>
    <tformat|<table|<row|<cell|<math-up|tan><around*|(|\<alpha\>|)>>|<cell|=>|<cell|d<rsub|>/<around*|(|r-h<rprime|''>|)>>>|<row|<cell|\<alpha\>>|<cell|=>|<cell|<math-up|atan><around*|(|<frac|d|r-h<rprime|''>>|)>>>>>
  </eqnarray*>

  <math|<wide|AB<rprime|''>|\<invbreve\>>=atan<around*|(|d/<around*|(|r-h<rprime|''>|)>|)>r>

  <subsubsection|Eight inches>

  <math|h=8\<times\>0.0254\<times\><around*|(|d/1609.34|)><rsup|2>>

  <subsubsection|Lets plot that>

  <big-figure|<image|code/gnuplot/eight_inches.eps|12cm|||>|>

  The approximation seems to work quite fine until medium distances (up to
  about <math|3000 km>).

  Zoom up to <math|1000 km>:

  <big-figure|<image|code/gnuplot/eight_inches_small.eps|12cm|||>|>

  <section|Shape of the horizon>

  <subsection|The question is not simple>

  What does the horizon looks like on a spherical Earth? We usually assume
  that the horizon is a ``line'' without really understanding its true shape.

  Of course, it cannot be a straight line, as when turning a bit on side, one
  again see a `straight `line'' not aligned with the first so first question
  is to compute what the horizon line is and how it change with altitude.

  Then, as most flatters rely on pictures, the question will be to understand
  how that line is projected on a picture when a camera shoot it.

  Then we'll be able to conclude.

  <subsection|Shape of the horizon line>

  <big-figure|<image|code/eukleides/horizon-line.eps|12cm|||>|<label|Fighl>>

  As seen on Figure <reference|Fighl>, the horizon seen from point A, pass by
  point B, but also by point B2. There is a symmetry of revolution around the
  vertical axis <math|OA>, so the horizon line is a circle of center
  <math|B<rprime|'>> and radius <math|l>.

  That's a very interesting point to notice, as a circle is not a straight
  line, and that one cannot apply the computation done in Section
  <reference|SectVanishing> to determine its ``curvature''. But the way, the
  ``curvature'' of the horizon is the curvature of the circle, and that
  cannot be seen easily from <math|A<rprime|'>>.

  <subsection|Properties of the horizon circle>

  Lets now compute this horizon circle properties. From Figure
  <reference|Fighl>, in the triangle <math|A<rprime|'>B<rprime|'>B>:

  <\equation>
    d<rsup|2><rsub|a>=<around*|(|h+h<rprime|'>|)><rsup|2>+l<rsup|2><label|eqhda>
  </equation>

  In the triangle <math|OB<rprime|'>B>:

  <\equation>
    r<rsup|2>=l<rsup|2>+<around*|(|r-h<rprime|'>|)><rsup|2><label|eqhr>
  </equation>

  <math|d<rsub|a>> is known from Equation <reference|eqda>, lets just sum the
  above two equations:

  <\eqnarray*>
    <tformat|<table|<row|<cell|d<rsup|2><rsub|a>+l<rsup|2>+<around*|(|r-h<rprime|'>|)><rsup|2>>|<cell|=>|<cell|<around*|(|h+h<rprime|'>|)><rsup|2>+l<rsup|2>+r<rsup|2>>>|<row|<cell|d<rsup|2><rsub|a>+r<rsup|2>+h<rprime|'><rsup|2>-2rh<rprime|'>>|<cell|=>|<cell|h<rsup|2>+h<rprime|'><rsup|2>+2hh<rprime|'>+r<rsup|2>>>|<row|<cell|d<rsup|2><rsub|a>-2rh<rprime|'>>|<cell|=>|<cell|h<rsup|2>+2hh<rprime|'>>>|<row|<cell|d<rsup|2><rsub|a>-h<rsup|2>>|<cell|=>|<cell|h<rprime|'><around*|(|2h+2r|)>>>|<row|<cell|h<rprime|'>>|<cell|=>|<cell|<frac|d<rsup|2><rsub|a>-h<rsup|2>|2h+2r>>>|<row|<cell|h<rprime|'>>|<cell|=>|<cell|<frac|h<rsup|2>+2rh-h<rsup|2>|2h+2r>>>|<row|<cell|h<rprime|'>>|<cell|=>|<cell|<frac|rh|r+h><eq-number><label|eqhp>>>>>
  </eqnarray*>

  Taking again Equation (<reference|eqhr>):

  <\eqnarray*>
    <tformat|<table|<row|<cell|r<rsup|2>>|<cell|=>|<cell|l<rsup|2>+<around*|(|r-h<rprime|'>|)><rsup|2>>>|<row|<cell|r<rsup|2>>|<cell|=>|<cell|l<rsup|2>+r<rsup|2>+h<rprime|'><rsup|2>-2rh<rprime|'>>>|<row|<cell|0>|<cell|=>|<cell|l<rsup|2>+<frac|r<rsup|2>h<rsup|2>|<around*|(|r+h|)><rsup|2>>-2r<frac|r<rsup|>h|r+h>>>|<row|<cell|0>|<cell|=>|<cell|l<rsup|2><around*|(|r+h|)><rsup|2>+r<rsup|2>h<rsup|2>-2r<rsup|2>h<around*|(|r+h|)>>>|<row|<cell|0>|<cell|=>|<cell|l<rsup|2><around*|(|r+h|)><rsup|2>+r<rsup|2>h<rsup|2>-2r<rsup|3>h-2r<rsup|2>h<rsup|2>>>|<row|<cell|0>|<cell|=>|<cell|l<rsup|2><around*|(|r+h|)><rsup|2>-2r<rsup|3>h-r<rsup|2>h<rsup|2>>>|<row|<cell|l<rsup|2><around*|(|r+h|)><rsup|2>>|<cell|=>|<cell|2r<rsup|3>h+r<rsup|2>h<rsup|2>>>|<row|<cell|l<rsup|2>>|<cell|=>|<cell|<frac|hr<rsup|2><around*|(|2r+h|)>|<around*|(|r+h|)><rsup|2>>>>|<row|<cell|l>|<cell|=>|<cell|r<frac|<sqrt|h<around*|(|2r+h|)>>|r+h><eq-number><label|eqhl>>>>>
  </eqnarray*>

  The radius and location of the horizon circle is now known.

  If we suppose a cartesian frame centered on <math|A>, with <math|y> as
  vertical axis, then, the equation of the circle can be wrote as:

  <\equation>
    <choice|<tformat|<table|<row|<cell|x<rsup|2>+z<rsup|2>=l<rsup|2>>>|<row|<cell|y=h<rprime|'>>>>>><label|eqhcircle>
  </equation>

  Note the fact that the equation impose <math|z\<in\><around*|[|-l,l|]>>, it
  will be used later.

  This is the equation of a circle of radiul <math|l> and center
  <math|B<rprime|'><around*|(|0,h<rprime|'>,0|)>> on plane
  <math|<around*|(|B<rprime|'>,x,z|)>>

  <subsection|Some words about camera projection>

  <subsubsection|The camera>

  Our model camera will be a perfect pinhole camera.

  <subsubsection|Horizontal camera>

  To simplify, we imagine that our camera is hold straight, so that the
  sensor is vertical and included in the <math|<around*|(|x,y|)>> plane. The
  hole located on the <math|y> axis at <math|P<around*|(|0,h,\<varepsilon\>|)>>.

  The projection equations in this case are very simple.

  \ <big-figure|<image|code/asymptote/pinholecamera.eps|12cm|||>|<label|FigPinHole>>

  From Figure <reference|FigPinHole>, we can see that the <math|x> and
  <math|y> coordinates are not mixed by the projection, so the computation of
  the transformation is easier.

  For a point <math|M<around*|(|x,y,z|)>>,
  <math|M<rprime|'><around*|(|x<rprime|'>,y<rprime|'>,z<rprime|'>|)>> being
  its projection on the sensor plane, using the notation of the Figure
  <reference|FigPinHole>, we get <math|M<rsub|xy>=<around*|(|x,0,z|)>>,
  <math|M<rsub|xy><rprime|'>=<around*|(|x<rprime|'>,0,z<rprime|'>|)>>,
  <math|M<rsub|yz>=<around*|(|0,y,z|)>> and
  <math|M<rsub|yz><rprime|'>=<around*|(|0,y<rprime|'>,z<rprime|'>|)>>.

  On the plane <math|xz>, line <math|M<rsub|xz>M<rprime|'><rsub|xz>>, defined
  by <math|x=az+b>:

  <\equation*>
    <choice|<tformat|<table|<row|<cell|0=a\<varepsilon\>+b\<Rightarrow\>b=-a\<varepsilon\>>>|<row|<cell|x=az+b>>>>>
  </equation*>

  Thus:

  <\equation*>
    a=<frac|x|z-\<varepsilon\>>
  </equation*>

  <\equation*>
    b=-a\<varepsilon\>=-<frac|\<varepsilon\>x|z-\<varepsilon\>>
  </equation*>

  In <math|M<rsub|xz><rprime|'>>, <math|z<rprime|'>=0>, so
  <math|x<rprime|'>=><math|<frac|-\<varepsilon\>x|z-\<varepsilon\>>>

  \;

  On the plane <math|yz>, line <math|OM<rsub|yz>>, defined by <math|y=az+b>:

  <\equation*>
    <choice|<tformat|<table|<row|<cell|h=a\<varepsilon\>+b\<Rightarrow\>b=h-a\<varepsilon\>>>|<row|<cell|y=az+b>>>>>
  </equation*>

  Thus:

  <\equation*>
    a=<frac|y-h|z-\<varepsilon\>>
  </equation*>

  In <math|M<rsub|yz><rprime|'>>, <math|y<rprime|'>=a*\<times\>0+b>:

  <\eqnarray*>
    <tformat|<table|<row|<cell|y<rprime|'>>|<cell|=>|<cell|<frac|h-y|z-\<varepsilon\>>\<varepsilon\>+h>>>>
  </eqnarray*>

  Finally:

  <\equation*>
    M<around*|(|x,y,z|)>\<Rightarrow\>M<rprime|'><choice|<tformat|<table|<row|<cell|x<rprime|'>=\<varepsilon\>x/z>>|<row|<cell|y<rprime|'>=<frac|y-h|z>\<varepsilon\>+h>>|<row|<cell|z<rprime|'>=\<varepsilon\>>>>>><label|eqmmp>
  </equation*>

  Lets rewrite this the other way:

  \;

  <\equation*>
    M<rprime|'><choice|<tformat|<table|<row|<cell|x=zx<rprime|'>/\<varepsilon\>>>|<row|<cell|z=\<varepsilon\><frac|y-h|y<rprime|'>-h>>>>>>
  </equation*>

  So

  \;

  <\equation>
    M<rprime|'><choice|<tformat|<table|<row|<cell|x=x<rprime|'><frac|y-h|y<rprime|'>-h>>>|<row|<cell|z=\<varepsilon\><frac|y-h|y<rprime|'>-h>>>>>><label|eqmpr>
  </equation>

  <subsection|Shape of the horizon viewed from an horizontal pinhole camera>

  Lets project the circle of horizon we defined in Equation
  (<reference|eqhcircle>), with the camera projection defined in Equation
  (<reference|eqmpr>). As the camera only see front, and to avoid
  divergeance, we'll limit the projection to <math|z\<gtr\>\<varepsilon\>>.
  We also have <math|\<varepsilon\>\<less\>l> (in fact
  <math|\<varepsilon\>\<ll\>l>):

  <\equation*>
    <tabular|<tformat|<table|<row|<cell|M<rprime|'>>|<cell|>|<cell|<choice|<tformat|<table|<row|<cell|x=x<rprime|'><frac|y-h|y<rprime|'>-h>>>|<row|<cell|z=\<varepsilon\><frac|y-h|y<rprime|'>-h>>>|<row|<cell|z
    \<in\><around*|[|\<varepsilon\>,l|]>>>|<row|<cell|x<rsup|2>+z<rsup|2>=l<rsup|2>>>|<row|<cell|y=h<rprime|'>>>>>>>>>>>
  </equation*>

  Posing <math|H=h<rprime|'>-h> and <math|Y<rprime|'>=y<rprime|'>-h>:

  <\eqnarray*>
    <tformat|<table|<row|<cell|<around*|(|<frac|Hx<rprime|'>|Y<rprime|'>>|)><rsup|2>+<around*|(|\<varepsilon\><frac|H|Y<rprime|'>>|)><rsup|2>>|<cell|=>|<cell|l<rsup|2>>>|<row|<cell|H<rsup|2>x<rprime|'><rsup|2>+\<varepsilon\><rsup|2>H<rsup|2>>|<cell|=>|<cell|l<rsup|2>Y<rprime|'><rsup|2>>>|<row|<cell|l<rsup|2>Y<rprime|'><rsup|2>-H<rsup|2>x<rprime|'><rsup|2>>|<cell|=>|<cell|\<varepsilon\><rsup|2>H<rsup|2>>>|<row|<cell|<frac|Y<rprime|'><rsup|2>|<frac|\<varepsilon\><rsup|2>H<rsup|2>|l<rsup|2>>>-<frac|x<rprime|'><rsup|2>|\<varepsilon\><rsup|2>>>|<cell|=>|<cell|1>>|<row|<cell|<frac|Y<rprime|'><rsup|2>|<around*|(|<frac|\<varepsilon\><rsup|>H<rsup|>|l<rsup|>>|)><rsup|2>>-<frac|x<rprime|'><rsup|2>|\<varepsilon\><rsup|2>>>|<cell|=>|<cell|1>>>>
  </eqnarray*>

  This is the equation of an hyperbole of parameters
  <math|a=><math|<frac|\<varepsilon\><rsup|>H<rsup|>|l<rsup|>>> and
  <math|b=\<varepsilon\>>

  <subsubsection|Plots>

  <\eqnarray*>
    <tformat|<table|<row|<cell|l<rsup|2>Y<rprime|'><rsup|2>-H<rsup|2>x<rprime|'><rsup|2>>|<cell|=>|<cell|\<varepsilon\><rsup|2>H<rsup|2>>>|<row|<cell|l<rsup|2>Y<rprime|'><rsup|2>>|<cell|=>|<cell|\<varepsilon\><rsup|2>H<rsup|2>+H<rsup|2>x<rprime|'><rsup|2>>>|<row|<cell|Y<rprime|'><rsup|2>>|<cell|=>|<cell|<frac|\<varepsilon\><rsup|2>H<rsup|2>+H<rsup|2>x<rprime|'><rsup|2>|l<rsup|2>>>>|<row|<cell|Y<rprime|'><rsup|>>|<cell|=>|<cell|<frac|1|l><sqrt|\<varepsilon\><rsup|2>H<rsup|2>+H<rsup|2>x<rprime|'><rsup|2>>>>|<row|<cell|Y<rprime|'><rsup|>>|<cell|=>|<cell|<frac|H|l><sqrt|\<varepsilon\><rsup|2>+x<rprime|'><rsup|2>>>>|<row|<cell|y<rprime|'><rsup|>>|<cell|=>|<cell|<frac|H|l><sqrt|\<varepsilon\><rsup|2>+x<rprime|'><rsup|2>>+h>>>>
  </eqnarray*>

  \;

  On Figure <reference|FigShape1>, we can see that for low altitude (here, up
  to <math|100 km>), the variation\ 

  <big-figure|<image|code/gnuplot/horizon_shape.eps|12cm|||>|<label|FigShape1>>
</body>

<\initial>
  <\collection>
    <associate|page-type|a4>
    <associate|par-hyphen|normal>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|FigEigthInches|<tuple|8|?>>
    <associate|FigPinHole|<tuple|12|?>>
    <associate|FigShape1|<tuple|13|?>>
    <associate|Fighl|<tuple|11|?>>
    <associate|Figure 1|<tuple|2|?>>
    <associate|SectVanishing|<tuple|3|?>>
    <associate|auto-1|<tuple|1|1>>
    <associate|auto-10|<tuple|2.3|2>>
    <associate|auto-11|<tuple|2.4|2>>
    <associate|auto-12|<tuple|2.5|2>>
    <associate|auto-13|<tuple|3|2>>
    <associate|auto-14|<tuple|3.1|2>>
    <associate|auto-15|<tuple|3.2|3>>
    <associate|auto-16|<tuple|3.2.1|3>>
    <associate|auto-17|<tuple|3|3>>
    <associate|auto-18|<tuple|3.2.2|3>>
    <associate|auto-19|<tuple|3.3|4>>
    <associate|auto-2|<tuple|1.1|1>>
    <associate|auto-20|<tuple|3.3.1|4>>
    <associate|auto-21|<tuple|3.3.2|4>>
    <associate|auto-22|<tuple|4|4>>
    <associate|auto-23|<tuple|3.4|5>>
    <associate|auto-24|<tuple|5|5>>
    <associate|auto-25|<tuple|3.5|?>>
    <associate|auto-26|<tuple|4|?>>
    <associate|auto-27|<tuple|4.1|?>>
    <associate|auto-28|<tuple|4.2|?>>
    <associate|auto-29|<tuple|6|?>>
    <associate|auto-3|<tuple|1|1>>
    <associate|auto-30|<tuple|4.3|?>>
    <associate|auto-31|<tuple|7|?>>
    <associate|auto-32|<tuple|4.4|?>>
    <associate|auto-33|<tuple|8|?>>
    <associate|auto-34|<tuple|4.4.1|?>>
    <associate|auto-35|<tuple|4.4.2|?>>
    <associate|auto-36|<tuple|4.4.3|?>>
    <associate|auto-37|<tuple|4.4.4|?>>
    <associate|auto-38|<tuple|4.4.5|?>>
    <associate|auto-39|<tuple|4.4.6|?>>
    <associate|auto-4|<tuple|1.2|1>>
    <associate|auto-40|<tuple|9|?>>
    <associate|auto-41|<tuple|10|?>>
    <associate|auto-42|<tuple|5|?>>
    <associate|auto-43|<tuple|5.1|?>>
    <associate|auto-44|<tuple|5.2|?>>
    <associate|auto-45|<tuple|11|?>>
    <associate|auto-46|<tuple|5.3|?>>
    <associate|auto-47|<tuple|5.4|?>>
    <associate|auto-48|<tuple|5.4.1|?>>
    <associate|auto-49|<tuple|5.4.2|?>>
    <associate|auto-5|<tuple|2|1>>
    <associate|auto-50|<tuple|12|?>>
    <associate|auto-51|<tuple|5.5|?>>
    <associate|auto-52|<tuple|5.5.1|?>>
    <associate|auto-53|<tuple|13|?>>
    <associate|auto-54|<tuple|13|?>>
    <associate|auto-6|<tuple|1.3|2>>
    <associate|auto-7|<tuple|2|2>>
    <associate|auto-8|<tuple|2.1|2>>
    <associate|auto-9|<tuple|2.2|2>>
    <associate|eq2|<tuple|3.3.2|4>>
    <associate|eqata|<tuple|4|?>>
    <associate|eqd|<tuple|1|?>>
    <associate|eqda|<tuple|3|?>>
    <associate|eqdb|<tuple|3|?>>
    <associate|eqhcircle|<tuple|9|?>>
    <associate|eqhda|<tuple|5|?>>
    <associate|eqhl|<tuple|8|?>>
    <associate|eqhp|<tuple|7|?>>
    <associate|eqhr|<tuple|6|?>>
    <associate|eqmmp|<tuple|12|?>>
    <associate|eqmpr|<tuple|10|?>>
    <associate|figatana|<tuple|7|?>>
    <associate|figflatflat|<tuple|1|?>>
    <associate|fighorizonplot|<tuple|4|?>>
    <associate|figmathorizon|<tuple|3|?>>
    <associate|figspacecurve|<tuple|2|?>>
    <associate|heq|<tuple|9|?>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|bib>
      BibWikiLoomingwiki:Looming
    </associate>
    <\associate|figure>
      <tuple|normal|(from a flatter post)|<pageref|auto-3>>

      <tuple|normal|(Credit NASA)|<pageref|auto-5>>

      <tuple|normal||<pageref|auto-17>>

      <tuple|normal||<pageref|auto-22>>

      <tuple|normal|Example of mirage and looming (credit :
      Wikipedia[<write|bib|BibWikiLoomingwiki:Looming><reference|bib-BibWikiLoomingwiki:Looming>])|<pageref|auto-24>>

      <tuple|normal||<pageref|auto-29>>

      <tuple|normal||<pageref|auto-31>>

      <tuple|normal||<pageref|auto-33>>

      <tuple|normal||<pageref|auto-40>>

      <tuple|normal||<pageref|auto-41>>

      <tuple|normal||<pageref|auto-45>>

      <tuple|normal||<pageref|auto-50>>

      <tuple|normal||<pageref|auto-53>>
    </associate>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|1<space|2spc>Presentation
      of the problem> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <with|par-left|<quote|1tab>|1.1<space|2spc>Flatters point of view
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2>>

      <with|par-left|<quote|1tab>|1.2<space|2spc>What some expects and why it
      doesnt have much meaning <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-4>>

      <with|par-left|<quote|1tab>|1.3<space|2spc>The questions we'll try to
      answer <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-6>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|2<space|2spc>Our
      tools> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-7><vspace|0.5fn>

      <with|par-left|<quote|1tab>|2.1<space|2spc>Mathematics
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-8>>

      <with|par-left|<quote|1tab>|2.2<space|2spc>Povray
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-9>>

      <with|par-left|<quote|1tab>|2.3<space|2spc>Data
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-10>>

      <with|par-left|<quote|1tab>|2.4<space|2spc>Globe model
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-11>>

      <with|par-left|<quote|1tab>|2.5<space|2spc>Flat Earth model
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-12>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|3<space|2spc>Disappearance
      beyond the horizon> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-13><vspace|0.5fn>

      <with|par-left|<quote|1tab>|3.1<space|2spc>Generalities
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-14>>

      <with|par-left|<quote|1tab>|3.2<space|2spc>Computation
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-15>>

      <with|par-left|<quote|2tab>|3.2.1<space|2spc>A bit of math
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-16>>

      <with|par-left|<quote|2tab>|3.2.2<space|2spc>Note about what we call
      distance between two points on Earth
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-18>>

      <with|par-left|<quote|1tab>|3.3<space|2spc>Numeric values
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-19>>

      <with|par-left|<quote|2tab>|3.3.1<space|2spc>First example and a useful
      remark <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-20>>

      <with|par-left|<quote|2tab>|3.3.2<space|2spc>Graphes
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-21>>

      <with|par-left|<quote|1tab>|3.4<space|2spc>A note about looming and
      mirages <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-23>>

      <with|par-left|<quote|1tab>|3.5<space|2spc>When observing, be precise
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-25>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|4<space|2spc>Height
      of the horizon> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-26><vspace|0.5fn>

      <with|par-left|<quote|1tab>|4.1<space|2spc>Presentation of the problem
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-27>>

      <with|par-left|<quote|1tab>|4.2<space|2spc>Computation
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-28>>

      <with|par-left|<quote|1tab>|4.3<space|2spc>Numerical values
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-30>>

      <with|par-left|<quote|1tab>|4.4<space|2spc>A note about ``8 inches per
      miles squared'' <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-32>>

      <with|par-left|<quote|2tab>|4.4.1<space|2spc>Computing
      <with|mode|<quote|math>|h<rprime|'>>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-34>>

      <with|par-left|<quote|2tab>|4.4.2<space|2spc>Computing length of arc
      \ <with|mode|<quote|math>|<wide|AB<rprime|'>|\<invbreve\>>>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-35>>

      <with|par-left|<quote|2tab>|4.4.3<space|2spc>Computing
      <with|mode|<quote|math>|h<rprime|''>>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-36>>

      <with|par-left|<quote|2tab>|4.4.4<space|2spc>Computing length of arc
      \ <with|mode|<quote|math>|<wide|AB<rprime|''>|\<invbreve\>>>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-37>>

      <with|par-left|<quote|2tab>|4.4.5<space|2spc>Eight inches
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-38>>

      <with|par-left|<quote|2tab>|4.4.6<space|2spc>Lets plot that
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-39>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|5<space|2spc>Shape
      of the horizon> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-42><vspace|0.5fn>

      <with|par-left|<quote|1tab>|5.1<space|2spc>The question is not simple
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-43>>

      <with|par-left|<quote|1tab>|5.2<space|2spc>Shape of the horizon line
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-44>>

      <with|par-left|<quote|1tab>|5.3<space|2spc>Properties of the horizon
      circle <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-46>>

      <with|par-left|<quote|1tab>|5.4<space|2spc>Some words about camera
      projection <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-47>>

      <with|par-left|<quote|2tab>|5.4.1<space|2spc>The camera
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-48>>

      <with|par-left|<quote|2tab>|5.4.2<space|2spc>Horizontal camera
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-49>>

      <with|par-left|<quote|1tab>|5.5<space|2spc>Shape of the horizon viewed
      from an horizontal pinhole camera <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-51>>

      <with|par-left|<quote|2tab>|5.5.1<space|2spc>Plots
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-52>>
    </associate>
  </collection>
</auxiliary>