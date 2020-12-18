# API

## Client

There is a `Client` class to instantiate that has methods to access the various supported **DraftKings** endpoints.

It can be `import`ed directly from the `draft_kings` module.

```python
from draft_kings import Client
```

## Enums

Various `enum` values are returned as part of the result set for API methods **_or_** as inputs for various API methods.

They are `import`ed from the `data` path.

=== "Sport"
    ```python
    from draft_kings.data import Sport
    ```
    
    !!! note
        Represents the various sports that **DraftKings** has contests for, like the NFL, MLB, and NBA


## Output

Data is returned as custom objects (and more specifically, instances of custom `Class`es that utilize the [`dataclasses`
 module](https://docs.python.org/3.7/library/dataclasses.html) - which is why this project relies on `Python 3.7+`).

The returned objects are (effectively) **immutable** via [`dataclasses`'s `frozen` property](https://docs.python.org/3.7/library/dataclasses.html#frozen-instances).

While immutability is just one reason behind using custom `Class`es, another benefit is making it easier to use this API
with the type-hinting features introduced in `Python 3`.

Using `Class`es with defined types makes it (hopefully) much easier to discern what the (theoretically) expected type of
any given field should be without having to print out some object.

The output objects are located in the `draft_kings.output.objects` module. There are sub-modules that correspond to each
 **DraftKings** endpoint.

### Why is (pretty much) every field `None`-able / `Optional` ?

This is a pretty explicit design decision I made when modeling the output data objects.

Because I don't have any control of the shape of the data returned by the **DraftKings** endpoints, if **DraftKings** 
decides tomorrow to remove a field, I figured it would be better to return the field with a `None` value vs. raising
some type of parsing / deserialization error.

So most of the fields will have the potential of a `None` value - however, there are some fields that are guaranteed to 
always have a non-`None` value. 

Please check the appropriate `Class`es defined in the `draft_kings.output.objects` 
module if you would like to see the defined return types.

## Methods

### Contests For A Given Sport

```python
from draft_kings import Sport, Client

Client().contests(sport=Sport.NBA)
```

### Available Players For A Given Draft Group

```python
from draft_kings import Client

Client().available_players(draft_group_id=41793)
```

### Details For A Given Draft Group

```python
from draft_kings import Client

Client().draft_group_details(draft_group_id=41793)
```

### Countries

```python
from draft_kings import Client

Client().countries()
```

### Regions For A Given Country

```python
from draft_kings import Client

Client().regions(country_code="US")
```

### Get Draftable Player / Match Up Informatiion For A Given Draft Group

```python
from draft_kings import Client

Client().draftables(draft_group_id=41793)
```

### Get Rules For A Game Type

```python
from draft_kings import Client

Client().game_type_rules(game_type_id=1)
```

### Usage

To the best of my knowledge, I have not identified an endpoint that delivers data for a window of time. 

So generally the usage pattern is something like

* Use the `contests` method to get the set of contests for all the `Sport`s you need data for
* These `Contests` will have `Draft Group`s associated with them - for each of these `Draft Group`s, use the related
  APIs to get the information you desire
* Depending on how frequently you need to display new information, you may need to repeat this set of operations as 
  there does not seem to be a an endpoint to subscribe to new `Contest`s or `Draft Group`s (or any type of data update, 
  in general)
