# Veri


Bu projede ESOGÜ kampüs haritasından alınarak oluşturulan XML formatında veriler kullanılmıştır. Bu veriler başka projelerde kullanıldığı için paylaşılamamaktadır. Fakat format olarak aşağıdaki gibi bir yapı kullanılmıştır.

```xml

<?xml version="1.0" encoding="UTF-8"?>

<Points>
    Talep olan noktalar
    <Point No="121" X="5182.387" Y="2937.322" lat="39.751670617892714" lon="30.480416670013025" Name="cs5" Type="Entrance" />
    <Point No="121" X="5182.387" Y="2937.322" lat="39.751670617892714" lon="30.480416670013025" Name="cs5" Type="Exit" />
    <Point No="121" X="5182.387" Y="2937.322" lat="39.751670617892714" lon="30.480416670013025" ChargingTime="900" Name="cs5" Type="DepoCharging" />

    <Point No="2" X="6202.75" Y="2938.383" lat="39.751938002852754" lon="30.49231551642376" Type="Delivery" Name="2">
        <Requests>
            <Request Product="A" Quantity="5" DueDate="303" TotalWeight="95" ServiceTime="120" ReadyTime="257" />
        </Requests>
    </Point>
    <Point No="37" X="5440.351" Y="2985.775" lat="39.752172063632734" lon="30.483409077029524" Type="Delivery" Name="39">
        <Requests>
            <Request Product="A" Quantity="1" DueDate="1578" TotalWeight="19" ServiceTime="120" ReadyTime="1523" />
        </Requests>
    </Point>
    . . . 
    Talep olmayan noktalar
    <Point No="1" X="6091.726" Y="3004.56" lat="39.75250570103818" lon="30.490999148931902" Type="Way" Name="1" />
    
    <Point No="3" X="5976.234" Y="2980.046" lat="39.75225589833148" lon="30.48966031185231" Type="Way" Name="3" />
    <Point No="4" X="6205.854" Y="2945.41" lat="39.752002037312934" lon="30.492349413277967" Type="Way" Name="4" />
    <Point No="5" X="6241.228" Y="3061.593" lat="39.75305678374528" lon="30.492723997544758" Type="Way" Name="5" />
    <Point No="6" X="5932.395" Y="2871.5" lat="39.75126775411403" lon="30.489184561590573" Type="Way" Name="6" />
    <Point No="7" X="5934.988" Y="2850.284" lat="39.75107743507831" lon="30.48922173857862" Type="Way" Name="7" />
    
</Points> 
```