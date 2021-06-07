---@class PeerStatus
---@field public ping number
---@field public quality_l number
---@field public quality_r number

---@class DS3Patch @parent class
---@field public get_peers fun():any[]
---@field public get_peer_status fun():(boolean, PeerStatus)
DS3Patch = {}
