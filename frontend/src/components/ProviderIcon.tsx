import { Provider } from "@/constants/Values";
import AsanaLogo from "@/assets/providers/asana.svg?react";
import JiraLogo from "@/assets/providers/jira.svg?react";
import AzureDevopsLogo from "@/assets/providers/azure_devops.svg?react";

const ProviderIcon = ({ provider }: { provider: Provider }) => {
    switch (provider) {
        case Provider.JIRA:
            return <JiraLogo />;
        case Provider.ASANA:
            return <AsanaLogo />;
        case Provider.AZURE_DEVOPS:
            return <AzureDevopsLogo />;
        default:
            return null;
    }
}

export default ProviderIcon;