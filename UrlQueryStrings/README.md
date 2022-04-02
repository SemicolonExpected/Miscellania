## getQueryStrings.py

Takes a textfile of urls and splits them into a dictionary of domains and a list of referer/referral ids pairs associated with the domain

Dictionary format  url => [{rid => referral string}, {rid => referral string}]

`--filter` filters out google trackers ie gclid, gclsrc by default. You can add or remove filtered out trackers on `line 17`

## scrapeLinks.py

`--filter` filters out facebook and amazon links, we can also define other link patterns to filter out

## Pipeline

urls.txt --> getQueryStrings --> check link for affiliate --> scrapeLinks unlabeled links --> check link for affiliates

- `DCLID` is doubleclick
- `h_ad_id` and `gc_id` is [HYROS](https://docs.hyros.com/how-to-connect-your-google-ads-to-hyros/), which tracks ads for conversions gcid specifically is for tracking google ads. Interestingly a lot of the sites that uses the Hyros trackers are webinars or "free book" sites. Interestingly the creator of Hyros is also one of these business "gurus"

- [`utm`](https://ga-dev-tools.web.app/ga4/campaign-url-builder/) stuff is adsense campaign related stuff

	- utm_term is paid keywords

- `ref`: if it is on an amazon link surprisingly it is just a regular amazon link. Ref in general (outside of amazon) is most likely an affiliate link
- `affid` `aff_c` or `aff_id` is very likely an affiliate link
- `afflilate` speaks for itself but it could be the companies own affiliate code not a third party's affiliate code

- `adp` indicates a group of similar clothing retailers like noracora.com www.hawalili.com justfashionnow.com etc
- `abtf2` sites with this parameter all get content from a site associated with malware in their `loadSuggestions()` function

`t.trklv.com` is [Prosper202](https://afflift.com/f/link-directory/prosper202.122/) a free tracker for affiliate marketters - arguably you can use it to track general ad campaigns but it is often used for affiliate marketting. Anysite using those links is an affiliate marketter.

`phr.htrackhq.com` is [TUNE](https://www.tune.com/) (it redirects to phr.hasoffers.com and if you go to just hasoffers.com it redirs to Tune) another affiliate marketing SaaS tool
`scmtrack.com`
`clickbank.net` links are definitely affiliate links
if a link on a page has track in it, I think it is probably it is an affiliate link
`wlg-scrty.com` is a tracking link

Sites with 'ac' 'ai' 'cr' "de" "dm" "kw" and 'ts' are all use the same site template (loads with 4 rotating semicirlces) ts: ytv I blieve means tracking source is youtube

<!--- 
A Primer on practices used to do Affiliate Marketting with paid advertisement.

1. Find offer to promote on sites like [OfferVault](offervault.com)
2. Make landing page for that product with affiliate links to or an embeded widget containing the advertised product's content/checkout 
3. Create advertisement on youtube, google, facebook or other advertisin gplatform leading to landing page.
4. ????
5. Profit

The advertiser creates an advertisement that leads to a landing page they created for the product they are advertising to look like they are the legitimate site for the product (merchant site). Depending on the payout model of the offer, a site might do different things.
- In **Pay per Sale** where the advertiser has to make a sale they could create pages with an embedded widgets that links to the merchant site's "add to cart" and "checkout" endpoints. When users try to buy from the advertiser's site they are actually buying the product from the merchant site while still on the fake site the advertiser created. The advertiser makes money because the links to the merchant site contains an affiliate code/tracker and thus the advertiser is credited as having closed the sale. Some 
- In **Pay per Lead** this would be the same except the endpoints would just be for the actions they want users to perform ie sign up for a newsletter/ download something/ watch a video etc
- In **Pay per Click** the advertiser just needs direct affiliate links to the site the merchant wants users to click on. They could also embedd it into their page so it could count as visiting the site when the embedded content loads.
--->