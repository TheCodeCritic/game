local status = script.Parent
local intermissionEvent = game.ReplicatedStorage.IntermissionEvent

intermissionEvent.OnClientEvent:Connect(function()
  for i = 20,0,-1 do
    status.Text = "New round starting in "..i
    wait(1)
  end
end
