## getQueryStrings.py

Takes a textfile of urls and splits them into a dictionary of domains and a list of referer/referral ids pairs associated with the domain

Dictionary format  url => [{rid => referral string}, {rid => referral string}]

`--filter` filters out google trackers ie gclid, gclsrc by default. You can add or remove filtered out trackers on `line 17`

- `DCLID` is doubleclick
- `h_ad_id` and `gc_id` is [HYROS](https://docs.hyros.com/how-to-connect-your-google-ads-to-hyros/), which tracks ads for conversions gcid specifically is for tracking google ads

- [`utm`](https://ga-dev-tools.web.app/ga4/campaign-url-builder/) stuff is adsense campaign related stuff

	- utm_term is paid keywords

- `ref`: if it is on an amazon link then it is an amazon associates (read: affiliates) link. Ref in general is most likely an affiliate link
- `affid` is very likely an affiliate link


