import ProviderIcon from "@/components/ProviderIcon";
import Colors from "@/constants/Colors";
import { Provider } from "@/constants/Values";

type ProjectHeaderProps = {
    projectName: string;
    provider: Provider;
}


const ProjectHeader = (props: ProjectHeaderProps) => {
    return (
        <div style={styles.backdropContainer}>
            <div style={styles.container} >
                <div style={styles.title}>
                    {props.projectName}
                </div>
                <div style={styles.icon}>
                    <ProviderIcon provider={props.provider} />
                </div>
            </div>
        </div>
    );
}

const styles = {
    backdropContainer: {
        backdropFilter: "blur(25px)",
        borderRadius: "40px 40px 0 0",
    },
    container: {
        padding: "30px 40px",
        display: "flex",
        justifyContent: "space-between",
        borderRadius: "40px 40px 0 0",
        opacity: "0.6",
        backgroundColor: Colors.white,
    },
    title: {
        fontSize: "35px",
        fontWeight: 500,
        color: Colors.black,
    },
    icon: {
        width: "50px",
        height: "50px",
    }
}

export default ProjectHeader;