"""
Contains various functions and classes that define the logic to turn the objects that represent the data
contained in DraftKings' endpoint responses, to the data returned by the client.

Sometimes, the data returned by the DraftKings' endpoints have fields that are not clearly named, or have field data
that can be converted to a more useful format.

For example, there are certain fields that are the string /Date(1606062600000)/. This string is probably in this format
to make it more immediately useful to be used the some JavaScript on the user's client.

However, this does not mean that this data is useful to the user of this DraftKings client API. So instead, the unix
timestamp should be parsed from the string and then returned as a datetime object.
"""
