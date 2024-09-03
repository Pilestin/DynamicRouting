
Bu klasörde osm.net.xml adında bir dosya olması gerekmekte. 
Bu dosya aşağıdaki gibi bir yapıya sahiptir : 

``` 

<net version="1.16" junctionCornerDetail="5" limitTurnSpeed="5.50" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/net_file.xsd">

    <location netOffset="-278956.86,-4400294.47" convBoundary="0.00,0.00,6315.04,4782.72" origBoundary="30.420349,39.725431,30.513154,39.768309" projParameter="+proj=utm +zone=36 +ellps=WGS84 +datum=WGS84 +units=m +no_defs"/>

    <type id="highway.cycleway" priority="1" numLanes="1" speed="5.56" allow="bicycle" oneway="0" width="1.00"/>
    <type id="highway.footway" priority="1" numLanes="1" speed="2.78" allow="pedestrian" oneway="1" width="2.00"/>
    <type id="highway.path" priority="1" numLanes="1" speed="5.56" allow="pedestrian bicycle" oneway="0" width="2.00"/>
    <type id="highway.pedestrian" priority="1" numLanes="1" speed="2.78" allow="pedestrian" oneway="1" width="2.00"/>
    . . . 
    . . . 

    <edge id=":2225294561_0" function="internal">
        <lane id=":2225294561_0_0" index="0" disallow="tram rail_urban rail rail_electric rail_fast ship" speed="5.56" length="9.63" shape="4860.35,2476.42 4859.91,2473.71 4858.82,2471.72 4857.07,2470.45 4854.68,2469.92"/>
    </edge>
    <edge id=":2225294561_1" function="internal">
        <lane id=":2225294561_1_0" index="0" disallow="tram rail_urban rail rail_electric rail_fast ship" speed="5.56" length="14.67" shape="4860.35,2476.42 4860.78,2472.36 4862.43,2469.56 4865.29,2468.04 4869.37,2467.79"/>
    </edge>
    <edge id=":2225294561_2" function="internal">
        <lane id=":2225294561_2_0" index="0" disallow="tram rail_urban rail rail_electric rail_fast ship" speed="3.65" length="4.67" shape="4860.35,2476.42 4861.10,2475.19 4861.89,2474.76 4862.70,2475.13 4863.55,2476.30"/>
    </edge>
    <edge id=":2225294561_3" function="internal">
        <lane id=":2225294561_3_0" index="0" disallow="tram rail_urban rail rail_electric rail_fast ship" speed="5.56" length="9.04" shape="4869.11,2470.98 4866.60,2471.13 4864.83,2472.07 4863.81,2473.79 4863.55,2476.30"/>
    </edge>
    . . . 
    . . .
    <junction id="2308050067" type="priority" x="4911.40" y="2732.15" incLanes="591658295#1_0 -221800343#4_0 221800343#3_0" intLanes=":2308050067_0_0 :2308050067_1_0 :2308050067_6_0 :2308050067_3_0 :2308050067_7_0 :2308050067_8_0" shape="4909.50,2736.94 4913.44,2736.91 4914.37,2724.95 4907.98,2725.16 4907.61,2727.37 4907.09,2728.16 4906.34,2728.74 4905.36,2729.11 4904.16,2729.28 4904.46,2735.67">
        <request index="0" response="000000" foes="010000" cont="0"/>
        <request index="1" response="000000" foes="110000" cont="0"/>
        <request index="2" response="001000" foes="001000" cont="1"/>
        <request index="3" response="000000" foes="000100" cont="0"/>
        <request index="4" response="000011" foes="000011" cont="1"/>
        <request index="5" response="000010" foes="000010" cont="1"/>
    </junction>
    <junction id="2308050070" type="right_before_left" x="4868.12" y="2733.23" incLanes="-221800344_0 -221800343#2_0 221800343#1_0" intLanes=":2308050070_0_0 :2308050070_1_0 :2308050070_2_0 :2308050070_3_0 :2308050070_4_0 :2308050070_5_0 :2308050070_6_0 :2308050070_7_0 :2308050070_8_0" shape="4865.58,2740.78 4872.08,2740.33 4872.01,2738.13 4872.43,2737.35 4873.16,2736.79 4874.20,2736.45 4875.54,2736.32 4875.45,2729.92 4861.03,2730.15 4861.14,2736.55 4863.10,2736.99 4863.91,2737.58 4864.59,2738.41 4865.15,2739.47">
        <request index="0" response="000000000" foes="100010000" cont="0"/>
        <request index="1" response="011000000" foes="011110000" cont="0"/>
        <request index="2" response="010001000" foes="010001000" cont="0"/>
        <request index="3" response="000000000" foes="010000100" cont="0"/>
        <request index="4" response="000000011" foes="110000011" cont="0"/>
        <request index="5" response="001000010" foes="001000010" cont="0"/>
        <request index="6" response="000000000" foes="000100010" cont="0"/>
        <request index="7" response="000011000" foes="000011110" cont="0"/>
        <request index="8" response="000010001" foes="000010001" cont="0"/>
    </junction>
    <junction id=":2225294604_7_0" type="internal" x="4826.89" y="2685.79" incLanes=":2225294604_1_0 212712115#8_0" intLanes=":2225294604_3_0 :2225294604_4_0 :2225294604_5_0 :2225294604_6_0"/>
    <junction id=":2225294627_7_0" type="internal" x="4701.88" y="2785.72" incLanes=":2225294627_6_0 -605647262#2_0" intLanes=":2225294627_1_0 :2225294627_2_0 :2225294627_3_0 :2225294627_4_0"/>
    <junction id=":2225294628_7_0" type="internal" x="4829.72" y="2801.30" incLanes=":2225294628_1_0 368611134#0_0" intLanes=":2225294628_3_0 :2225294628_4_0 :2225294628_5_0 :2225294628_6_0"/>
    . . . 
    . . .
    <connection from="-699418305#1" to="-699418305#0" fromLane="0" toLane="0" via=":6567842067_2_0" dir="s" state="M"/>
    <connection from="-699418305#1" to="699418303#1" fromLane="0" toLane="0" via=":6567842067_3_0" dir="l" state="m"/>
    <connection from="-699418305#2" to="-699418305#1" fromLane="0" toLane="0" via=":6567868490_0_0" dir="s" state="M"/>
    <connection from="-699418305#2" to="699418308#0" fromLane="0" toLane="0" via=":6567868490_1_0" dir="l" state="m"/>
    . . . 
    . . . 
    <roundabout nodes="2225294912 2225294921 2225294964 3724717208" edges="1060234726#1 1060234726#2 1060234726#3 1060234726#4"/>
    <roundabout nodes="3724621935 3724621943 3724621952 3724621956 3734084494" edges="368610900#1 368610900#2 368610900#3 368610900#4 368610900#5"/>
    <roundabout nodes="2225294895 2225294962 2225294963 3734058871" edges="369625684#1 369625684#2 369625684#3 369625684#4"/>
    <roundabout nodes="3742378309 3742378310 3742378323" edges="370540854#1 370540854#2 642121506#1"/>

</net>

``` 