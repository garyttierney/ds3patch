register_callback("on_gui", function()
    ImGui.Begin("DS3 Patch Debugger")

    ImGui.Text("Total peers: " .. #DS3Patch.get_peers())
    ImGui.Columns(3)
    ImGui.Text("Ping")
    ImGui.NextColumn()
    ImGui.Text("Quality (local)")
    ImGui.NextColumn()
    ImGui.Text("Quality (remote)")
    ImGui.NextColumn()

    for _, peer in ipairs(DS3Patch.get_peers()) do
        success, peer_stats = DS3Patch.get_peer_status(peer)

        if success then
            ImGui.Text(tostring(peer_stats.ping))
            ImGui.NextColumn()
            ImGui.Text(tostring(peer_stats.quality_local))
            ImGui.NextColumn()
            ImGui.Text(tostring(peer_stats.quality_remote))
            ImGui.NextColumn()
        end
    end

    ImGui.Columns()
    ImGui.End()
end)