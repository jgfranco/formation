'''
When traveling around a city on public transit, changing busses or trains can be time consuming. We're building an app to help people plan routes and minimize transfers.

We'll be given routes as an array and each route is a list of stops along the route. We can assume that busses move back and forth along the routes so no matter the order of stops along any route, we can reach all stops along that route with one ride.

The stops themselves are represented as positive integers.

Given the list of routes and a desired starting stop and destination stop, what is the minimum number of bus rides required to reach the destination? If the destination stop is not reachable, return -1.
 

EXAMPLE(S)
Consider routes:
[
  [1, 2, 7],
  [3, 6, 7]
]
stop 1 -> 6
1 -> 2 -> 7 (2 BUSES)
          -> 2
          -> 6
  -> 7 -> (6)
       -> 2

1: (2,7)
2: (7, 1)
3: (6, 1)
7:(3,6, 1, 2)

{node: set(node)}

for each route:
  for each node:
      map[node].add(set(route))


If we want to get from stop 1 to stop 6, we can take the first bus to stop 7, then transfer and take the second bus to stop 6 for 2 rides to reach the destination.

For for routes [[1, 2,3], [4, 5, 6]], notice we can't transfer between routes. So there is no way to start at stop 1 and arrive at stop 5. In this case, return -1.
 

FUNCTION SIGNATURE
function numBusesToDestination(routes, source, target)
def num_busses_to_destination(routes, source, target):
'''

def buildAdjecencyList(routes):
  adjList = {}
  for route in routes:
    for stop in route:
      adjList[stop] = route
  
  return adjList

def numBusesToDestination(routes, source, target):

    adjList = buildAdjecencyList(routes)
    if len(adjList) ==0: return -1

    from collections import deque
    q = deque([(source, 0)])

    visited = set()

    while q:
      currStop, buses = q.popleft()

      if currStop not in visited:
            
        if currStop == target:
          return buses
            
        for stop in adjList[currStop]:
          q.append((stop, buses+1))

        visited.add(currStop)

    return -1

print(numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6) == 2)
print(numBusesToDestination([[2], [2, 8]], 8, 2) == 1)
print(numBusesToDestination([[2], [2, 8]], 8, 7) == -1)
print(numBusesToDestination(
  [
    [1, 9, 12, 20, 23, 24, 35, 38],
    [10, 21, 24, 31, 32, 34, 37, 38, 43],
    [10, 19, 28, 37],
    [8],
    [14, 19],
    [11, 17, 23, 31, 41, 43, 44],
    [21, 26, 29, 33],
    [5, 11, 33, 41],
    [4, 5, 8, 9, 24, 44]],
  37, 28) == 1)
print(numBusesToDestination([], 1, 6) == -1)
print(numBusesToDestination([[]], 1, 6) == -1)
print(numBusesToDestination([[1, 2, 3]], 1, 1) == 0)
print(numBusesToDestination([[1, 2, 3]], 1, 3) == 1)



"""
to study some other day... maybe

function numBusesToDestination(routes, source, target) {
  if (source === target) return 0;

  // convert routes to sets for easy look ups
  for (let i = 0; i < routes.length; i++) {
    routes[i] = new Set(routes[i]);
  }

  // Build a map of stop numbers to a set of
  // route numbers that serve that stop
  const busStopRoutes = new Map();
  for (let i = 0; i < routes.length; i++) {
    const route = routes[i];
    for (const stopId of route) {
      let routesForStop = busStopRoutes.get(stopId);
      if (!routesForStop) {
        routesForStop = new Set();
        busStopRoutes.set(stopId, routesForStop);
      }
      routesForStop.add(i);
    }
  }

  // keep track of a set of stops we can reach as we BFS routes
  const reachableStops = new Set([source]);
  // keep track of routes used so we don't infinite loop
  const routesUsed = new Set();
  // Start with the set of routes served by the source stop
  let routesToTry = busStopRoutes.get(source) || new Set();
  // Anything we can get to on that first bus is one ride away
  let rideCount = 1;

  while (routesToTry.size > 0 && !reachableStops.has(target)) {
    const nextRoutes = new Set();

    for (const routeId of routesToTry) {
      // Look at stops served by this route
      for (const stopId of routes[routeId]) {
        // Only process stops we haven't seen via previous routes
        if (!reachableStops.has(stopId)) {
          if (stopId === target) return rideCount;
          reachableStops.add(stopId);

          // add potential transfers we haven't seen before from this new stop
          for (const transferRouteId of busStopRoutes.get(stopId)) {
            if (!routesUsed.has(transferRouteId)) {
              nextRoutes.add(transferRouteId);
              routesUsed.add(transferRouteId);
            }
          }
        }
      }
    }

    rideCount++;
    routesToTry = nextRoutes;
  }

  return -1;
}
"""