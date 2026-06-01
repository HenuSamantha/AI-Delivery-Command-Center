type ConnectedSourcesProps = {
    jiraTickets: any[];
    slackMessages: string[];
  };
  
  export default function ConnectedSources({
    jiraTickets,
    slackMessages,
  }: ConnectedSourcesProps) {
    return (
      <div className="bg-gray-900 p-6 rounded-2xl border border-gray-800 mb-8">
        <h2 className="text-2xl font-semibold mb-6">
          Connected Sources
        </h2>
  
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
  
          <div>
            <h3 className="text-lg font-semibold mb-3 text-blue-400">
              Jira Tickets
            </h3>
  
            {jiraTickets.map((ticket) => (
              <div
                key={ticket.key}
                className="mb-2 text-gray-300"
              >
                <strong>{ticket.key}</strong> | {ticket.status}
                <br />
                {ticket.title}
              </div>
            ))}
          </div>
  
          <div>
            <h3 className="text-lg font-semibold mb-3 text-green-400">
              Slack Signals
            </h3>
  
            {slackMessages.map((message, index) => (
              <div
                key={index}
                className="mb-2 text-gray-300"
              >
                • {message}
              </div>
            ))}
          </div>
  
        </div>
      </div>
    );
  }