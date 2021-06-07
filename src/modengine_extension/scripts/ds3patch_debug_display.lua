callbacks = { gui = on_gui }


local function on_gui()

    if not ImGui.Begin("test") then
        return
    end

    ImGui.Text("Test")

    ImGui.End()
end

