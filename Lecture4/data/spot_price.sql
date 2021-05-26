--rignore
DECLARE @_startdate AS DATE = '2019-01-01'
DECLARE @_enddate AS DATE = '2019-02-01'
DECLARE @_datasource AS NVARCHAR(MAX) = 'EPEX'
--end


SELECT	DateValueCET AS ValueDate, 
		DATEPART(HOUR, ValueDateTimeOffset) + 1 AS Hourcet, 
		PriceMWh

FROM	DPA_MarketData.dpv.FactPowerSpotPriceActual

WHERE	PowerPriceArea = 'Germany'
AND		DateValueCET BETWEEN @_startdate AND @_enddate
AND		DataSource = @_datasource
AND		Granularity = 'hour'

ORDER BY ValueDateTimeOffset