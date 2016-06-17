<TeXmacs|1.99.2>

<style|article>

<\body>
  <\doc-data|<doc-title|Some notes about plane trips length and shape of the
  Earth>|<doc-author|<\author-data|<author-name|TK>>
    \;
  <|author-data>
    \;
  <|author-data>
    \;
  </author-data>>>
    \;
  </doc-data>

  <section|Presentation>

  The idea is to collect timetables of direct flights between different
  cities (better using mean value between two directions to avoid dominant
  winds effects). Then postulating that the time of fglight is likled to the
  actual disance between two cities by a simple relation. We'll pose
  <math|T=a+b D>, where <math|T> is the time of flight, <math|a> a constant
  (that take into account boarding time, take-off and landing, etc.),
  <math|b> a speed, and D the actual distance.

  With a few cities of known distances we fit the data to get the best
  <math|a> and <math|b> vales. Then we can use the equation to infer
  distances between other cities.

  By wisely choosing the cities, we expect to conclude that no flat model can
  works.

  <section|Calibration>

  Using know distances to calibrate our function:

  The following table was used, data from http://maps.google.fr:

  <small-table|<tabular|<tformat|<table|<row|<cell|From>|<cell|To>|<cell|Time>|<cell|(to>|<cell|from)>|<cell|Distance>>|<row|<cell|Paris>|<cell|London>|<cell|1:10:00>|<cell|1:10:00>|<cell|1:10:00>|<cell|200>>|<row|<cell|Paris>|<cell|Buccuresti>|<cell|2:57:30>|<cell|2:50:00>|<cell|3:05:00>|<cell|1868>>|<row|<cell|Paris
  >|<cell|Warsaw>|<cell|2:15:00>|<cell|2:10:00>|<cell|2:20:00>|<cell|1368>>|<row|<cell|>|<cell|>|<cell|>|<cell|>|<cell|>|<cell|>>|<row|<cell|>|<cell|>|<cell|>|<cell|>|<cell|>|<cell|>>>>>|>

  FROM \ \ \ \ \ \ \ \ \ \ \ TO \ \ \ \ \ \ \ \ \ \ \ \ \ \ TIME \ \ \ \ (To
  \ \ \ \ \ \ \ \ From \ \ \ \ ) \ \ \ \ \ \ \ \ D1 \ \ \ \ \ \ D2 ( Err)

  Paris \ \ \ \ \ \ \ -\<gtr\> London \ \ \ \ \ \ : ( \ 1:10:00 ( \ - \ \ )
  \ ) : \ \ 200

  Paris \ \ \ \ \ \ \ -\<gtr\> \ \ \ : ( \ \ ( \ - \ \ ) \ ) : \ 1868

  \;

  Paris \ \ \ \ \ \ \ -\<gtr\> Berlin \ \ \ \ \ \ : ( \ 1:40:00 ( 1:35:00 -
  \ 1:45:00 ) \ ) : \ \ 800

  Paris \ \ \ \ \ \ \ -\<gtr\> Moscow \ \ \ \ \ \ : ( \ 3:37:30 ( 3:25:00 -
  \ 3:50:00 ) \ ) : \ 2485

  \;

  <include|toto.tm>

  <include|code/python/fittable.tm>

  <section|Deducing distances>

  \;

  \;
</body>

<\initial>
  <\collection>
    <associate|page-type|a4>
    <associate|par-hyphen|normal>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|FigEigthInches|<tuple|6|?>>
    <associate|FigPinHole|<tuple|10|?>>
    <associate|FigShape1|<tuple|11|?>>
    <associate|Fighl|<tuple|9|?>>
    <associate|Figure 1|<tuple|2|?>>
    <associate|SectVanishing|<tuple|3|?>>
    <associate|auto-1|<tuple|1|1>>
    <associate|auto-10|<tuple|2.5|2>>
    <associate|auto-11|<tuple|3|2>>
    <associate|auto-12|<tuple|3.1|2>>
    <associate|auto-13|<tuple|3.2|2>>
    <associate|auto-14|<tuple|3.2.1|2>>
    <associate|auto-15|<tuple|1|3>>
    <associate|auto-16|<tuple|3.2.2|3>>
    <associate|auto-17|<tuple|3.3|3>>
    <associate|auto-18|<tuple|3.3.1|3>>
    <associate|auto-19|<tuple|3.3.2|4>>
    <associate|auto-2|<tuple|2|1>>
    <associate|auto-20|<tuple|2|4>>
    <associate|auto-21|<tuple|3.4|4>>
    <associate|auto-22|<tuple|3|4>>
    <associate|auto-23|<tuple|3.5|5>>
    <associate|auto-24|<tuple|4|5>>
    <associate|auto-25|<tuple|4.1|?>>
    <associate|auto-26|<tuple|4.2|?>>
    <associate|auto-27|<tuple|4|?>>
    <associate|auto-28|<tuple|4.3|?>>
    <associate|auto-29|<tuple|5|?>>
    <associate|auto-3|<tuple|1|1>>
    <associate|auto-30|<tuple|4.4|?>>
    <associate|auto-31|<tuple|6|?>>
    <associate|auto-32|<tuple|4.4.1|?>>
    <associate|auto-33|<tuple|4.4.2|?>>
    <associate|auto-34|<tuple|4.4.3|?>>
    <associate|auto-35|<tuple|4.4.4|?>>
    <associate|auto-36|<tuple|4.4.5|?>>
    <associate|auto-37|<tuple|4.4.6|?>>
    <associate|auto-38|<tuple|7|?>>
    <associate|auto-39|<tuple|8|?>>
    <associate|auto-4|<tuple|2|1|toto.tm>>
    <associate|auto-40|<tuple|5|?>>
    <associate|auto-41|<tuple|5.1|?>>
    <associate|auto-42|<tuple|5.2|?>>
    <associate|auto-43|<tuple|9|?>>
    <associate|auto-44|<tuple|5.3|?>>
    <associate|auto-45|<tuple|5.4|?>>
    <associate|auto-46|<tuple|5.4.1|?>>
    <associate|auto-47|<tuple|5.4.2|?>>
    <associate|auto-48|<tuple|10|?>>
    <associate|auto-49|<tuple|5.5|?>>
    <associate|auto-5|<tuple|3|1>>
    <associate|auto-50|<tuple|5.5.1|?>>
    <associate|auto-51|<tuple|11|?>>
    <associate|auto-52|<tuple|12|?>>
    <associate|auto-53|<tuple|13|?>>
    <associate|auto-54|<tuple|13|?>>
    <associate|auto-6|<tuple|2.1|2>>
    <associate|auto-7|<tuple|2.2|2>>
    <associate|auto-8|<tuple|2.3|2>>
    <associate|auto-9|<tuple|2.4|2>>
    <associate|eq2|<tuple|3.3.2|4>>
    <associate|eqata|<tuple|4|?>>
    <associate|eqd|<tuple|1|?>>
    <associate|eqda|<tuple|1|?>>
    <associate|eqdb|<tuple|3|?>>
    <associate|eqhcircle|<tuple|9|?>>
    <associate|eqhda|<tuple|5|?>>
    <associate|eqhl|<tuple|8|?>>
    <associate|eqhp|<tuple|7|?>>
    <associate|eqhr|<tuple|6|?>>
    <associate|eqmmp|<tuple|10|?>>
    <associate|eqmpr|<tuple|10|?>>
    <associate|figatana|<tuple|5|?>>
    <associate|figflatflat|<tuple|1|?>>
    <associate|fighorizonplot|<tuple|2|?>>
    <associate|figmathorizon|<tuple|1|?>>
    <associate|figspacecurve|<tuple|1|?>>
    <associate|heq|<tuple|9|?>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|table>
      <tuple|normal||<pageref|auto-3>>

      <tuple|normal||<pageref|auto-4>>
    </associate>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|1<space|2spc>Presentation>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|2<space|2spc>Calibration>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|3<space|2spc>Deducing
      distances> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-5><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>