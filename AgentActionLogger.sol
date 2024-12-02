// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AgentActionLogger {
    // Struct to hold details of each action
    struct Action {
        address agent;
        string actionType;
        string details;
        uint256 timestamp;
        string txHash;
    }

    // Array to store all actions
    Action[] public actions;

    // Mapping to fetch actions by ID
    mapping(uint256 => Action) public actionById;

    // Event that will be emitted when an action is logged
    event ActionLogged(
        uint256 indexed id,
        address indexed agent,
        string actionType,
        string details,
        uint256 timestamp,
        string txHash
    );

    // Function to log actions on-chain
    function logAction(
        string memory actionType,
        string memory details,
        string memory txHash
    ) public {
        uint256 id = actions.length;  // Generate a unique ID for this action

        // Push the action details into the actions array
        actions.push(Action(msg.sender, actionType, details, block.timestamp, txHash));
        actionById[id] = actions[id];  // Store the action in the mapping

        // Emit the event with the action details
        emit ActionLogged(id, msg.sender, actionType, details, block.timestamp, txHash);
    }

    // Function to get details of a specific action by ID
    function getAction(uint256 id) public view returns (Action memory) {
        require(id < actions.length, "Action does not exist");
        return actions[id];
    }

    // Function to get all logged actions
    function getActions() public view returns (Action[] memory) {
        return actions;
    }
}
