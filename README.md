# swarmops-contracts

The single source of truth for every message that crosses a process boundary in SwarmOps.
Everything else (backend, console, fleet-sim) depends on the packages generated here.

| Package | Path | Consumers |
|---|---|---|
| `.proto` sources | `proto/swarmops/**` | — |
| Go module `github.com/swarm-ops/swarmops-contracts/gen/go` | `gen/go` | swarmops-backend |
| npm `@swarmops/contracts` | `gen/ts` | swarmops-console |
| Python `swarmops-contracts` (import `swarmops`) | `gen/python` | swarmops-fleet-sim, backend planner |

> `github.com/swarm-ops` is a placeholder owner. Find/replace it with your GitHub user/org
> in this repo and in `swarmops-backend` before pushing.

## Packages

- `swarmops.drone.v1`: drone ↔ backend messages over MQTT (telemetry, commands, acks, events)
- `swarmops.realtime.v1`: console ↔ gateway WebSocket frames
- `swarmops.control.v1`: `FleetService`, the operator API (Connect-RPC)
- `swarmops.planner.v1`: `PlannerService`, the internal planning API (gRPC)

## MQTT topics

| Topic | Payload | Direction | QoS |
|---|---|---|---|
| `swarm/v1/{fleet_id}/{drone_id}/telemetry` | `drone.v1.Telemetry` | drone → backend | 0 |
| `swarm/v1/{fleet_id}/{drone_id}/cmd` | `drone.v1.Command` | backend → drone | 1 |
| `swarm/v1/{fleet_id}/{drone_id}/ack` | `drone.v1.CommandAck` | drone → backend | 1 |
| `swarm/v1/{fleet_id}/{drone_id}/event` | `drone.v1.DroneEvent` | drone → backend | 1 |

All payloads are binary protobuf.

## Working on contracts

No local protoc or plugins are needed: `buf` comes from npm, and the plugins run remotely on the BSR.

```bash
npx @bufbuild/buf lint
npx @bufbuild/buf breaking --against '.git#branch=main'
npx @bufbuild/buf generate          # writes gen/{go,ts/src,python/src}
(cd gen/ts && npm install && npm run build)
```

Generated code **is committed**. Go consumers import it directly from git, and CI fails if it drifts.

## Compatibility rules

- Within `v1`, changes are additive only: new fields, messages, RPCs or enum values. `buf breaking` enforces this.
- Never reuse or renumber a field. Use `reserved` when removing one.
- A breaking change means a new `v2` package, served alongside `v1` until all consumers move.

## Releasing

Push a tag `vX.Y.Z`. The `release` workflow:
1. tags the Go submodule as `gen/go/vX.Y.Z` (Go requires the path prefix for nested modules),
2. publishes `@swarmops/contracts@X.Y.Z` to GitHub Packages (npm),
3. builds the Python wheel and attaches it to the GitHub release.

Until the first release, the sibling repos consume this repo through local paths
(`replace` in `go.mod`, `file:` in `package.json`, a path source in `pyproject.toml`).
