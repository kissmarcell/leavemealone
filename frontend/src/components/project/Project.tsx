import ProjectBody from "@/components/project/ProjectBody";
import ProjectHeader from "@/components/project/ProjectHeader";
import { ProjectType } from "@/types/project";

type ProjectProps = {
    project: ProjectType;
};

const Project = (props: ProjectProps) => {
    return (
        <div style={styles.container}>
            <ProjectHeader projectName={props.project.name} provider={props.project.provider} />
            <ProjectBody issues={props.project.issues} />
        </div>
    );
}

const styles = {
    container: {
        display: "flex",
        flexDirection: "column",
        color: "#fff",
        margin: "10px 150px",
        borderRadius: "40px 40px 25px 25px",
        boxShadow: "1px 1px 6px black",
    }
} as const;

export default Project;