QueryMarks = '''
select gps.FestivalCode, gps.FestivalYear, gps.EntryId, gps.mark1,gps.mark2,gps.mark3,gps.mark4,
gps.Split1Percentage,gps.Split2Percentage,gps.Split3Percentage,gps.Split4Percentage, gps.Total, gps.SplitDesc,
ec.FestivalCode, ec.EntryTypeName as Award, ec.MediaDescription, ec.CategoryDescription as "Category Description",
ED.Advertiser, ED.short as Shortlist,  ed.EntryId as "All Entries",ed.Product, ed.Title,
ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode as "Cat Code", ed.CatalogueNo,
cd.CompanyName, CD.NetworkCode, cd.NetworkName, CD.UltimateHoldingCompanyName,  
cd.Country, cd.GroupCompanyName, cd.coTown, cd.CompanyType, cd.RegionName



from GrandPrixSplits gps

inner join ArchiveEntryData ed
	on ed.EntryId = gps.entryid
	and ed.FestivalYear = gps.FestivalYear
	and ed.FestivalCode = gps.FestivalCode  COLLATE Latin1_General_CI_AI


left Join ArchiveCompanyData as CD
	on ED.EntrantCompanyNo = CD.companyNo 
	and ed.Festivalyear = cd.ArchiveYear

inner join ArchiveEntryCategories ec
    
	ON ec.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ed.FestivalYear
	AND ec.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ed.EntryTypeId

order by gps.FestivalYear
'''


DirectAndFilm = '''
SELECT 
cd.companyName, cd.Country, cd.coTown, cd.NetworkName, cd.UltimateHoldingCompanyName, cd.RegionName,
ED.Advertiser, ED.short as Shortlist,  ed.EntryId as "All Entries",ed.Product, ed.Title,
ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode as "Cat Code", ed.CatalogueNo,
ed.FestivalCode, ed.FestivalYear, 

ec.EntryTypeName, ec.MediaDescription,
ec.CategoryDescription as "Category Description",
em.Mark, em.Split1, em.split2, em.split3, em.split4, em.RoundOfVoting,
emm.MarkWeighting, emm.split1q, emm.split2q, emm.split3q, emm.split4q,
emm.SplitDesc

FROM  vw_ArchiveEntryData ED

inner join CL2021..EntryMarks em
	on ed.EntryId = em.EntryId

inner join iaff..ArchiveCompanyData as CD
	on ED.EntrantCompanyNo = CD.companyNo 
	and ed.Festivalyear = cd.ArchiveYear

inner join iaff..ArchiveEntryCategories ec

	ON ec.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ed.FestivalYear
	AND ec.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ed.EntryTypeId


inner join cl2021..entry_markMethod emm
	on ec.EntryTypeId = emm.EntryTypeId
	and emm.RoundOfVoting = em.RoundOfVoting
    
where ed.FESTIVALCODE IN ('CL', 'LE', 'LI', 'LH')
and( ec.EntryTypeName = 'film'
or ec.EntryTypeName = 'direct')

'''



queryStandard = '''
	SELECT 
ed.FestivalCode, ed.FestivalYear, em.EntryId, em.mark,em.Split1, em.Split2, em.Split3,em.Split4,
emm.Split1q,emm.Split2q,emm.Split3q,emm.Split4q, em.CalcMark, emm.SplitDesc,
ec.FestivalCode, ec.EntryTypeName as Award, ec.MediaDescription, ec.CategoryDescription as "Category Description",
ED.Advertiser, ED.short as Shortlist,  ed.EntryId as "All Entries",ed.Product, ed.Title,
ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode as "Cat Code", ed.CatalogueNo,
cd.CompanyName, cd.NetworkCode,cd.NetworkName, cd.UltimateHoldingCompanyName,
cd.Country, cd.GroupCompanyName, cd.coTown, cd.CompanyType,cd.RegionName


	FROM  vw_ArchiveEntryData ED

	inner join CL2019..EntryMarks em
		on ed.EntryId = em.EntryId

	inner join iaff..ArchiveCompanyData as CD
		on ED.EntrantCompanyNo = CD.companyNo 
		and ed.Festivalyear = cd.ArchiveYear

	inner join iaff..ArchiveEntryCategories ec

		ON ec.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
		AND ec.FestivalYear = ed.FestivalYear
		AND ec.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
		AND ec.EntryTypeId = ed.EntryTypeId


	inner join cl2019..entry_markMethod emm
		on ec.EntryTypeId = emm.EntryTypeId
		and emm.RoundOfVoting = em.RoundOfVoting
	

	where ed.FESTIVALCODE IN ('CL', 'LE', 'LI', 'LH')
	and ed.AwardCountCode like 'gp'
	and ec.EntryTypeName = 'direct'

'''


queryAlMarks ='''
SELECT 
	ed.FestivalCode, ed.FestivalYear, ed.Title, ed.EntryTypeName as "Lion",
	ED.short as Shortlist, ED.AwardCountCode as Winner,  
	em.EntryId as "All Entries" ,em.RoundOfVoting, em.Mark,em.Split1,em.Split2,em.Split3,em.Split4,em.Split5, 
	emm.Split1q,emm.Split2q,emm.Split3q,emm.Split4q,emm.Split5q,emm.SplitDesc,
	cd.CompanyName, cd.NetworkName, cd.UltimateHoldingCompanyName,
	cd.Country, cd.coTown

FROM  iaff..ArchiveEntryData ED

inner join %s..EntryMarks em
	on ed.EntryId = em.EntryId
	
inner join %s..entry_markMethod emm
	on ed.EntryTypeId = emm.EntryTypeId
	and emm.RoundOfVoting = em.RoundOfVoting

inner join iaff..ArchiveCompanyData as CD
	on ED.EntrantCompanyNo = CD.companyNo 
	and ed.Festivalyear = cd.ArchiveYear

where ed.FESTIVALCODE IN ('CL', 'LE', 'LI', 'LH')
	and ed.Short =1
	and ed.festivalyear = %s
'''
