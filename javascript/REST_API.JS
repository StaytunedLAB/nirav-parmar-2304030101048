import { Octokit } from "@octokit/core";
import 'dotenv/config'; // Loads .env automatically

const octokit = new Octokit({
    auth: ""
});

/**
 * Create a new GitHub issue
 */
export async function createIssue(title, body, labels = ['Task']) {
    try {
        await octokit.request('POST /repos/{owner}/{repo}/issues', {
            owner: process.env.REPO_OWNER,
            repo: process.env.REPO_NAME,
            title,
            body,
            labels,
            headers: {
                'X-GitHub-Api-Version': '2022-11-28'
            }
        });
        console.log("✅ Issue created successfully");
    } catch (error) {
        console.error("❌ Error creating issue:", error.message);
    }
}
